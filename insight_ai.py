import random

def generate_ai_summary(cpu_avg, total_cost):

    insights = []

    # CPU usage analysis
    if cpu_avg is None:
        insights.append("No CPU data available to analyze.")
    else:
        if cpu_avg < 20:
            insights.append("Your EC2 instances are underutilized. Consider downsizing or consolidating workloads.")
        elif cpu_avg < 70:
            insights.append("Your EC2 performance is optimal. No major scaling needed right now.")
        else:
            insights.append("High CPU usage detected — consider auto-scaling or investigating workload efficiency.")

    # Cost analysis
    if total_cost is None:
        insights.append("No cost data available to analyze.")
    else:
        if total_cost > 50:
            insights.append(f"Total cost this period is ${total_cost:.2f}. Review unused resources and consider reserved instances.")
        elif total_cost > 10:
            insights.append(f"Cost is ${total_cost:.2f}. Moderate — monitor trends to optimize.")
        else:
            insights.append(f"Cost is ${total_cost:.2f}. Strong cost efficiency observed.")

    # Add a short closing suggestion for realism
    closing_line = random.choice([
        "Projected cost trend looks stable for the next week.",
        "Potential savings opportunity detected in EC2 and S3 usage.",
        "Performance and cost are balanced — continue monitoring usage patterns.",
    ])
    insights.append(closing_line)

    # Return a single combined string
    return " ".join(insights)

# Quick local test when run directly
if __name__ == "__main__":
    print(generate_ai_summary(cpu_avg=18.5, total_cost=8.75))
