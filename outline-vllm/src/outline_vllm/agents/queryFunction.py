import json
from utilities.prompts import generate_hermes_prompt
from agents.reactAgent import Decision
from agents.reactAgent import wikipedia


def query(question, chatbot, max_turns=5):
    i = 0
    next_prompt = (
        "\n<|im_start|>user\n" + question + "<|im_end|>" "\n<|im_start|>assistant\n"
    )
    previous_actions = []
    while i < max_turns:
        i += 1
        prompt = generate_hermes_prompt(
            question=question, schema=Decision.model_json_schema()
        )
        bot = chatbot(prompt=prompt)
        result = bot(next_prompt)
        json_result = json.loads(result)["Decision"]
        if "Final_Answer" not in list(json_result.keys()):
            scratchpad = json_result["Scratchpad"] if i == 0 else ""
            thought = json_result["Thought"]
            action = json_result["Action"]
            action_input = json_result["Action_Input"]
            print(f"\x1b[34m Scratchpad: {scratchpad} \x1b[0m")
            print(f"\x1b[34m Thought: {thought} \x1b[0m")
            print(f"\x1b[36m  -- running {action}: {str(action_input)}\x1b[0m")
            if action + ": " + str(action_input) in previous_actions:
                observation = (
                    "You already run that action. **TRY A DIFFERENT ACTION INPUT.**"
                )
            else:
                if action == "calculate":
                    try:
                        observation = eval(str(action_input))
                    except Exception as e:
                        observation = f"{e}"
                elif action == "wikipedia":
                    try:
                        observation = wikipedia(str(action_input))
                    except Exception as e:
                        observation = f"{e}"
            print()
            print(f"\x1b[33m Observation: {observation} \x1b[0m")
            print()
            previous_actions.append(action + ": " + str(action_input))
            next_prompt += (
                "\nScratchpad: "
                + scratchpad
                + "\nThought: "
                + thought
                + "\nAction: "
                + action
                + "\nAction Input: "
                + action_input
                + "\nObservation: "
                + str(observation)
            )
        else:
            scratchpad = json_result["Scratchpad"]
            final_answer = json_result["Final_Answer"]
            print(f"\x1b[34m Scratchpad: {scratchpad} \x1b[0m")
            print(f"\x1b[34m Final Answer: {final_answer} \x1b[0m")
            return final_answer
    print(
        "\nFinal Answer: I am sorry, but I am unable to answer your question. Please provide more information or a different question."
    )
    return "No answer found"
