import boto3
import datetime

cloudwatch = boto3.client('cloudwatch', region_name='ap-south-1')
ce = boto3.client('ce', region_name='ap-south-1')

def get_avg_cpu():
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(hours=24)
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        StartTime=start,
        EndTime=end,
        Period=3600,
        Statistics=['Average']
    )
    if not response['Datapoints']:
        return "No EC2 data available."
    avg = sum(dp['Average'] for dp in response['Datapoints']) / len(response['Datapoints'])
    return f"Average CPU Utilization (24 hrs): {avg:.2f}%"

def get_daily_cost():
    end = datetime.date.today()
    start = end - datetime.timedelta(days=1)
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start.strftime('%Y-%m-%d'), 'End': end.strftime('%Y-%m-%d')},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    if not response['ResultsByTime']:
        return "No cost data found."
    amount = float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])
    return f"AWS Cost ({start} → {end}): ${amount:.4f}"

def build_report():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    cpu = get_avg_cpu()
    cost = get_daily_cost()

    report = f"""
===============================
 AWS Smart Cloud Dashboard Report
===============================
Generated at: {now}

{cpu}
{cost}

Insights:
- If CPU > 70%, investigate EC2 workload.
- If daily cost > $1, check Cost Explorer service breakdown.

Next Step → Send this report to Bedrock for AI summary.
===============================
"""
    with open("daily_report.txt", "w") as f:
        f.write(report)
    print("✅ Report generated: daily_report.txt")

if __name__ == "__main__":
    build_report()
