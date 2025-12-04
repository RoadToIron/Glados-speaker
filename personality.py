from transformers import pipeline

class Personality:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')
        self.prompt = f" You are GLaDOS from portal you are witty and sarcastic, i will ask you something then you answer the question is: "
    def Respond(self,Dialogue):
        input_text = self.prompt + Dialogue + " now respond"
        response = self.generator(input_text, max_length=150,temperature=0.7,do_sample=True,repetition_penalty=1.2)
        print(f"input_text: {input_text}")
        garbage_len = len(input_text)
        response=response[garbage_len:]
        print(response)
        return(response)

Glados=Personality()
response=Glados.Respond("hello glados its me aly mosselhi i heard you ran some experiments today tell me about them.")
print(response[0]['generated_text'])