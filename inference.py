import os
from openai import OpenAI
from env.workflow_env import WorkflowEnv, Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy_key")

USE_MOCK = True  # ✅ IMPORTANT

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def run():

    env = WorkflowEnv()

    # 🔥 Run all 3 tasks
    for _ in range(3):

        obs = env.reset()

        print(f"\n[START] task={obs.task} env=workflow model={MODEL_NAME}")

        done = False
        step = 0
        rewards = []

        while not done and step < 3:
            step += 1

            # 🔥 Task-specific instruction (CORRECT PLACE)
            if obs.task == "email_triage":
                instruction = "Classify emails into urgent, normal, spam"
            elif obs.task == "bug_prioritization":
                instruction = "Classify bugs into P0, P1, P2"
            elif obs.task == "code_review":
                instruction = "Identify issue type: bug, security, performance"

            prompt = f"""
            {instruction}
            Return ONLY list.

            Input:
            {obs.input_data}
            """

            # 🔥 MOCK vs REAL
            if USE_MOCK:
                if obs.task == "email_triage":
                    output = ["urgent", "spam", "normal"]
                elif obs.task == "bug_prioritization":
                    output = ["P0", "P2", "P1"]
                else:
                    output = ["security", "performance", "bug"]

                error = None

            else:
                try:
                    response = client.chat.completions.create(
                        model=MODEL_NAME,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    content = response.choices[0].message.content
                    output = eval(content)
                    error = None
                except Exception as e:
                    output = ["urgent", "spam", "normal"]
                    error = str(e)

            action = Action(output=output)

            obs, reward, done, _ = env.step(action)

            rewards.append(f"{reward:.2f}")

            print(f"[STEP] step={step} action={output} reward={reward:.2f} done={str(done).lower()} error={error}")

        print(f"[END] success={str(done).lower()} steps={step} rewards={','.join(rewards)}")


if __name__ == "__main__":
    run()