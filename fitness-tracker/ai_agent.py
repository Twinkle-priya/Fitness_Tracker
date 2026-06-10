import subprocess

def get_cluster_data():
    return subprocess.getoutput("kubectl get all -A")

def main():
    data = get_cluster_data()

    print("\n===== CLUSTER SNAPSHOT =====\n")
    print(data)

    print("\n===== AI ANALYSIS =====\n")
    if "CrashLoopBackOff" in data:
        print("Issue: Pods are crashing. Fix image/env/logs.")
    elif "Error" in data:
        print("Issue: Kubernetes error detected.")
    else:
        print("Cluster looks healthy. No critical issues detected.")

if __name__ == "__main__":
    main()
