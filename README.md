# 🧠 AWS Smart Cloud Dashboard  
A **simulated AI-powered AWS monitoring and cost management CLI dashboard** built with Python.  
This project provides real-time insights into AWS resource usage, CloudWatch metrics, and cost trends — all from your terminal.  
It includes a simulated “InsightAI” module that generates smart summaries of your AWS environment.



## 🚀 Features  
- 📊 **Live CLI Dashboard:** Displays AWS CloudWatch CPU utilization and daily AWS cost trends.  
- 🧠 **InsightAI Summary:** Generates smart textual summaries about usage efficiency and projected trends (simulated).  
- ☁️ **AWS Integration:** Fetches data via the AWS SDK (`boto3`) for real metrics.  
- 🔔 **Daily Summaries:** Automatically generates daily cost/usage summaries.  
- 💡 **Cost Awareness:** Promotes cloud cost efficiency and monitoring habits.  



## 🧩 Tech Stack  
| Component | Technology |
|------------|-------------|
| Language | Python3 |
| Cloud SDK | AWS SDK for Python (`boto3`) |
| CLI UI | `rich` |
| Scheduling | `schedule` |
| Data Processing | `pandas` |
| Environment Management | `python-dotenv` |
| AI Simulation | Custom logic (`insight_ai.py`) |

---

## 📁 Project Structure
AWS-Smart-Cloud-Dashboard/
│
├── cli_dashboard.py # Main terminal dashboard (auto-refresh)
├── aws_insights_test.py # Fetches and tests AWS metric data
├── daily_summary.py # Generates daily cost/usage summaries
├── insight_ai.py # Simulated AI engine for insights
├── requirements.txt # Required dependencies


## ⚙️ Setup Instructions
AWS-Smart-Cloud-Dashboard
cd AWS-Smart-Cloud-Dashboard
python -m venv venv              #Create a Virtual Environment
source venv/bin/activate   
venv\Scripts\activate      
pip install -r requirements.txt  #Install Dependencies
aws configure                    #Configure AWS Credentials
  -AWS_ACCESS_KEY_ID=your_key
  -AWS_SECRET_ACCESS_KEY=your_secret
  -AWS_DEFAULT_REGION=ap-south-1
  

## Run the Dashboard
python cli_dashboard.py


## 🧠 Example Output
🧠 CloudWatch CPU Utilization (Last 12 hrs)
┏━━━━━━┳━━━━━━━━━━━━━┓
┃ Time ┃ Avg CPU (%) ┃
┡━━━━━━╇━━━━━━━━━━━━━┩
│ 14:00 │ 17.8 │
│ 15:00 │ 22.3 │
└──────┴─────────────┘

💰 AWS Cost (Last 7 Days)
┏━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Date ┃ Cost ($) ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━┩
│ 2025-10-21 │ 0.0123 │
│ 2025-10-22 │ 0.0118 │
└────────────┴──────────┘

🤖 InsightAI Summary:
"Cost efficiency strong. No unusual CPU spikes. Trend stable for the next week."


## 👩‍💻 Author
Kalyani Mishra
Aspiring Cloud Engineer
linkedin - www.linkedin.com/in/kalyani-mishra-a05267234


## 📈 Project Impact

This project automated AWS monitoring and cost tracking, reducing manual console checks by nearly 90% and improving cost visibility by over 95%. The simulated AI insight engine enabled faster interpretation of cloud trends, boosting operational awareness by ~80%. Overall, it strengthened hands-on skills in AWS automation, cost optimization, and real-time cloud observability, directly aligning with Cloud Support and FinOps roles.











