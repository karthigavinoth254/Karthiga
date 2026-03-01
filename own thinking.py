#word counting
text = input("Enter a sentence: ")
words = text.split()
word_count = len(words)
print("number of words: ",word_count)
#vowels counting(1)
name=input("enter the sentence:")
vowels=[x for x in name if x.lower()in 'aeiou']
print(vowels)

#frequency program using count
import re

text = """AI Engineer with of experience designing and deploying
production-grade AI agents and Retrieval-Augmented
Generation (RAG) systems using Python, LangChain,
and Google Gemini API.
Experienced in building scalable LLM-powered applications. Strong expertise in prompt engineering, embeddings, vector databases (FAISS/Chroma). Passionate about operationalizing AI solutions that align with business analytics and decision intelligence systems."""

words = re.findall(r'\b\w+\b', text.lower())

words = {w: sum(1 for x in words if x == w) for w in set(words)}

print("{" + ", ".join([f"key={i} : value={j}" for i, j in words.items()]) + "}")
