🧠
AutoResQ: An Intelligent Disaster Recovery & Rollback Platform for Cloud-Native Deployments

🚀 Overview
In modern cloud-native applications, continuous deployments and high availability are crucial. However, deployment of faulty updates or unexpected infrastructure failures (like EC2 crashes, AZ outages, or network partitions) can lead to significant downtime and data loss.
AutoResQ aims to solve this by:

🔁 Automating application deployment with intelligent monitoring and rollback
💥 Simulating real-world cloud disasters (infrastructure & logical errors) using AWS Lambda
🛠️ Automatically triggering recovery workflows using predefined strategies

Jenkins Pipeline overview
![image](https://github.com/user-attachments/assets/03330c5a-87db-46d4-ae82-da41594bfbe7)
![image](https://github.com/user-attachments/assets/1d9a8c30-1e1f-42ab-92b5-41ac418bc714)

🧩 Key Components
Stack	Tools
CI/CD	 -  Jenkins, Git/GitLab, Webhooks
Containerization  - 	Docker, Kubernetes
Cloud Infra  - 	AWS (EC2, Lambda, S3, Redis, CloudWatch)
Monitoring  - 	Prometheus + Grafana
Disaster Simulation  - 	Lambda-triggered chaos functions
Rollbacks  - 	Git + Helm/K8s + Jenkins scripted rollback, version-controlled
APIs  - 	REST APIs to initiate/simulate failures or query deployment status

⚙️ How It Works
Code Push to Git → Jenkins Trigger
Jenkins picks up changes and builds Docker images → pushes to ECR → deploys to Kubernetes via Helm.

Monitoring & Health Checks
Prometheus scrapes metrics from apps, Redis, and EC2 instances.
Grafana displays dashboards with alerting set up via AlertManager (email/Slack/webhook).

Disaster Simulation Module (Lambda)
AWS Lambda functions scheduled (e.g. via EventBridge) to randomly:

Terminate EC2 instances

-Simulate AZ outage (e.g. by tainting K8s nodes or shutting down services in a region)
-Block network access (via NACL/Security Group modification)
-Trigger a faulty update (i.e. bad container version)
-Auto Detection & Rollback

Jenkins receives alerts (via Prometheus Alertmanager webhook receiver)
→ Checks which release caused degradation
→ Triggers Helm rollback to previous known-good deployment
→ Logs event in S3 for audit/training

Recovery Automation
In case of infra failures, Lambda triggers recovery routines:

Replace failed EC2s (Auto Scaling)

Restore from backups (Redis snapshots or S3)

Re-route traffic or re-spin apps in another AZ

📈 Real-World Relevance
This project mirrors real enterprise needs:

High availability and fault tolerance are must-haves in production.

Teams push changes rapidly → automated rollback prevents outages.

Cloud-native systems must simulate and plan for disaster recovery.

Think of this as a mini version of Netflix’s Chaos Monkey, combined with real-time deployment rollback and auto-healing.

📊 Success Metrics
✅ Time to recovery after each simulated failure

✅ Accuracy of rollback detection and rollback time

✅ Deployment pipeline success/failure ratio

✅ Visualization of metrics in Grafana dashboard

✅ System uptime across chaos scenarios


## 📦 Features

- ✅ Flask App with Prometheus metrics endpoint (`/metrics`)
- ✅ Docker-based containerization
- ✅ Kubernetes deployment on Minikube (running on EC2)
- ✅ Monitoring with Prometheus & Grafana
- ✅ Jenkins-based CI/CD pipeline
- ✅ Port-forwarding and external access via NodePort
- ✅ AWS EC2 hosted setup (Ubuntu-based instance)


Ensure the following are installed on your **AWS EC2 instance**:
- Docker
- kubectl
- Minikube
- Helm
- Jenkins
- Git
- Python 3.9+

  
🔒 Stretch Goals
Add Slack or Discord bot integration to notify team about incidents, rollbacks, or recovery

Incorporate machine learning later to predict failures based on Prometheus metrics
