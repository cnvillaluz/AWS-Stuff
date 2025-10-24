# Module 2.3: Jobs and CronJobs

## Jobs

Jobs create one or more pods and ensure a specified number complete successfully.

### When to Use Jobs

- Batch processing
- Data processing tasks
- Database migrations
- Backup operations
- One-time administrative tasks

### Simple Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi-calculation
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl:5.34
        command: ["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```

### Job with Completions

Run job multiple times sequentially.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: batch-job
spec:
  completions: 5  # Run 5 times
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["/bin/sh", "-c", "echo Processing item $RANDOM && sleep 5"]
      restartPolicy: Never
```

### Parallel Jobs

Run multiple pods in parallel.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel-job
spec:
  completions: 10
  parallelism: 3  # Run 3 pods at a time
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["/bin/sh", "-c", "echo Processing && sleep 10"]
      restartPolicy: Never
```

### Job Patterns

#### 1. Work Queue Pattern

Multiple pods process items from queue.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: work-queue
spec:
  parallelism: 5  # 5 workers
  completions: 10  # 10 total items
  template:
    spec:
      containers:
      - name: worker
        image: work-queue-processor:latest
        env:
        - name: QUEUE_URL
          value: "redis://queue-service:6379"
      restartPolicy: OnFailure
```

#### 2. Fixed Completion Count

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: fixed-job
spec:
  completions: 8  # Exactly 8 completions needed
  parallelism: 2   # 2 at a time
  template:
    spec:
      containers:
      - name: worker
        image: worker:latest
      restartPolicy: OnFailure
```

### Job Configuration

#### Restart Policy

```yaml
spec:
  template:
    spec:
      restartPolicy: Never  # or OnFailure
```

- **Never**: Create new pod on failure
- **OnFailure**: Restart container on failure
- **Always**: NOT allowed for Jobs

#### Backoff Limit

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: retry-job
spec:
  backoffLimit: 6  # Retry up to 6 times
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["sh", "-c", "exit 1"]  # Will fail
      restartPolicy: Never
```

#### Active Deadline

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: timeout-job
spec:
  activeDeadlineSeconds: 100  # Job terminates after 100s
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["sleep", "300"]
      restartPolicy: Never
```

#### TTL After Finished

Automatic cleanup after completion.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: cleanup-job
spec:
  ttlSecondsAfterFinished: 100  # Delete 100s after completion
  template:
    spec:
      containers:
      - name: worker
        image: busybox
        command: ["echo", "done"]
      restartPolicy: Never
```

### Managing Jobs

```bash
# Create Job
kubectl create -f job.yaml

# Imperative creation
kubectl create job test-job --image=busybox -- echo "Hello"

# Get Jobs
kubectl get jobs
kubectl get jobs --watch

# Describe Job
kubectl describe job pi-calculation

# Get pods from job
kubectl get pods --selector=job-name=pi-calculation

# Get Job logs
kubectl logs job/pi-calculation

# Delete Job
kubectl delete job pi-calculation

# Delete Job but keep pods
kubectl delete job pi-calculation --cascade=orphan
```

### Job Status

```bash
# Check completion
kubectl get job pi-calculation -o yaml | grep -A 5 status

# Fields:
# - active: Running pods
# - succeeded: Successfully completed pods
# - failed: Failed pods
```

## CronJobs

CronJobs create Jobs on a schedule (like cron in Linux).

### CronJob YAML

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup-job
spec:
  schedule: "0 2 * * *"  # Every day at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: backup-tool:latest
            command: ["/bin/sh", "-c", "echo Backing up database"]
          restartPolicy: OnFailure
```

### Cron Schedule Format

```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
# │ │ │ │ │
# * * * * *
```

### Common Schedules

```yaml
# Every minute
schedule: "* * * * *"

# Every hour
schedule: "0 * * * *"

# Every day at midnight
schedule: "0 0 * * *"

# Every day at 2:30 AM
schedule: "30 2 * * *"

# Every Monday at 8 AM
schedule: "0 8 * * 1"

# Every 15 minutes
schedule: "*/15 * * * *"

# First day of month at midnight
schedule: "0 0 1 * *"

# Weekdays at 9 AM
schedule: "0 9 * * 1-5"
```

### CronJob Configuration

#### Concurrency Policy

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: scheduled-job
spec:
  schedule: "*/1 * * * *"
  concurrencyPolicy: Allow  # Allow, Forbid, or Replace
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: worker
            image: busybox
            command: ["sleep", "120"]
          restartPolicy: OnFailure
```

- **Allow**: Multiple jobs can run concurrently (default)
- **Forbid**: Skip new job if previous still running
- **Replace**: Cancel current and start new job

#### Starting Deadline

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: deadline-job
spec:
  schedule: "*/1 * * * *"
  startingDeadlineSeconds: 100  # Start within 100s or count as missed
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: worker
            image: busybox
          restartPolicy: Never
```

#### Job History

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: history-job
spec:
  schedule: "*/5 * * * *"
  successfulJobsHistoryLimit: 3  # Keep last 3 successful
  failedJobsHistoryLimit: 1       # Keep last 1 failed
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: worker
            image: busybox
          restartPolicy: Never
```

#### Suspend CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: suspended-job
spec:
  schedule: "*/1 * * * *"
  suspend: true  # Don't create new jobs
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: worker
            image: busybox
          restartPolicy: Never
```

### Managing CronJobs

```bash
# Create CronJob
kubectl create -f cronjob.yaml

# Imperative creation
kubectl create cronjob test-job --image=busybox --schedule="*/1 * * * *" -- echo "Hello"

# Get CronJobs
kubectl get cronjobs
kubectl get cj

# Describe CronJob
kubectl describe cronjob backup-job

# Get jobs created by CronJob
kubectl get jobs --selector=cronjob=backup-job

# Suspend CronJob
kubectl patch cronjob backup-job -p '{"spec":{"suspend":true}}'

# Resume CronJob
kubectl patch cronjob backup-job -p '{"spec":{"suspend":false}}'

# Delete CronJob
kubectl delete cronjob backup-job

# Manually trigger CronJob
kubectl create job manual-backup --from=cronjob/backup-job
```

### Complete CronJob Example

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: database-backup
  namespace: production
spec:
  schedule: "0 2 * * *"  # 2 AM daily
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  startingDeadlineSeconds: 300
  jobTemplate:
    spec:
      backoffLimit: 3
      activeDeadlineSeconds: 3600
      template:
        metadata:
          labels:
            app: backup
        spec:
          restartPolicy: OnFailure
          containers:
          - name: backup
            image: postgres:14
            env:
            - name: PGPASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: password
            command:
            - /bin/sh
            - -c
            - |
              pg_dump -h database-service -U postgres mydb > /backup/backup-$(date +%Y%m%d).sql
              echo "Backup completed"
            volumeMounts:
            - name: backup-storage
              mountPath: /backup
          volumes:
          - name: backup-storage
            persistentVolumeClaim:
              claimName: backup-pvc
```

## CKA Exam Tips

### Jobs
- Know different job patterns (completions, parallelism)
- Understand restart policies for jobs
- Practice creating jobs imperatively: `kubectl create job`
- Know how to check job status and logs
- Understand backoffLimit and activeDeadlineSeconds
- Practice with ttlSecondsAfterFinished for cleanup

### CronJobs
- Memorize cron schedule syntax
- Know concurrency policies (Allow, Forbid, Replace)
- Practice creating cronjobs: `kubectl create cronjob`
- Know how to suspend/resume cronjobs
- Understand job history limits
- Practice manually triggering jobs from cronjobs

## Practice Exercises

1. Create a simple job that prints "Hello World"
2. Create a job with 5 completions
3. Create a parallel job with 3 workers
4. Set backoffLimit and test failure handling
5. Create CronJob that runs every minute
6. Create CronJob with Forbid concurrency policy
7. Suspend and resume a CronJob
8. Manually trigger a job from CronJob
9. Check job history
10. Create backup CronJob with PVC

## Troubleshooting

```bash
# Job not completing
kubectl describe job <job-name>
kubectl logs job/<job-name>
kubectl get pods -l job-name=<job-name>

# CronJob not creating jobs
kubectl describe cronjob <name>
kubectl get cronjob <name> -o yaml  # Check suspend field
kubectl get events --sort-by=.metadata.creationTimestamp

# Job pods failing
kubectl get pods -l job-name=<job-name>
kubectl logs <pod-name>
kubectl describe pod <pod-name>
```

## Quick Reference

```bash
# Jobs
kubectl create job myjob --image=busybox -- echo "Hello"
kubectl get jobs
kubectl logs job/myjob
kubectl delete job myjob

# CronJobs
kubectl create cronjob myjob --image=busybox --schedule="*/1 * * * *" -- echo "Hello"
kubectl get cronjobs
kubectl get cj
kubectl create job manual --from=cronjob/myjob
kubectl patch cronjob myjob -p '{"spec":{"suspend":true}}'
kubectl delete cronjob myjob
```

## Next Steps

Move to Module 2.4: RBAC and Security
