# Delete-OldSnapshots.ps1
# Deletes EC2 snapshots owned by your account that are older than 6 months.
# Requires: AWS CLI configured with appropriate permissions (ec2:DescribeSnapshots, ec2:DeleteSnapshot)

param(
    [string]$Region = "us-east-1",
    [int]$MonthsOld = 6,
    [switch]$DryRun,
    [string]$OwnerAlias = "self"
)

$cutoffDate = (Get-Date).AddMonths(-$MonthsOld)
$cutoffDateUtc = $cutoffDate.ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

Write-Host "Scanning for snapshots older than $MonthsOld months (before $($cutoffDate.ToString('yyyy-MM-dd')))..."
if ($DryRun) {
    Write-Host "[DRY RUN] No snapshots will actually be deleted." -ForegroundColor Yellow
}

# Fetch all snapshots owned by the account
$snapshotsJson = aws ec2 describe-snapshots `
    --owner-ids $OwnerAlias `
    --region $Region `
    --query "Snapshots[?StartTime<='$cutoffDateUtc'].[SnapshotId,StartTime,Description,VolumeSize]" `
    --output json 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to retrieve snapshots. Check your AWS CLI configuration and permissions."
    Write-Error $snapshotsJson
    exit 1
}

$snapshots = $snapshotsJson | ConvertFrom-Json

if ($snapshots.Count -eq 0) {
    Write-Host "No snapshots found older than $MonthsOld months." -ForegroundColor Green
    exit 0
}

Write-Host "Found $($snapshots.Count) snapshot(s) to delete:" -ForegroundColor Cyan

$deleted = 0
$failed = 0

foreach ($snap in $snapshots) {
    $snapId   = $snap[0]
    $snapDate = $snap[1]
    $snapDesc = $snap[2]
    $snapSize = $snap[3]

    Write-Host "  $snapId  |  $snapDate  |  ${snapSize}GB  |  $snapDesc"

    if (-not $DryRun) {
        $result = aws ec2 delete-snapshot --snapshot-id $snapId --region $Region 2>&1
        if ($LASTEXITCODE -eq 0) {
            $deleted++
        } else {
            Write-Warning "  Failed to delete $snapId : $result"
            $failed++
        }
    }
}

if ($DryRun) {
    Write-Host "`n[DRY RUN] Would have deleted $($snapshots.Count) snapshot(s)." -ForegroundColor Yellow
} else {
    Write-Host "`nDone. Deleted: $deleted  |  Failed: $failed" -ForegroundColor Green
}
