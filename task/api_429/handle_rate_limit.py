import time
import requests

def get_with_retry(url, max_retries=3, default_wait=5):

    for attempt in range(1, max_retries + 1):
        response = requests.get(url)

        if response.status_code == 200:
            print(f"✅ Success on attempt {attempt}")
            return response

        elif response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            wait_time = int(retry_after) if retry_after else default_wait
            print(f"⚠️ Rate limit hit (429). Waiting {wait_time}s before retry {attempt}/{max_retries}...")
            time.sleep(wait_time)
        else:
            response.raise_for_status()

    raise Exception(f"❌ Failed after {max_retries} retries due to rate limiting.")
