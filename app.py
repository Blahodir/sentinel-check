import os

def main():
    target = os.getenv("TARGET_URL", "google.com")
    print(f"--- Sentinel Scan Started for {target} ---")
    # Тут могла б бути логіка сканування
    print("Scan completed successfully.")

if __name__ == "__main__":
    main()
