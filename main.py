import string

n_docs = int(input("Liczba dokumentów do przetworzenia (n): "))
print()

docs = []

for i in range(n_docs):
    doc_n = input(f"Wprowadź wielowyrazowy dokument {i+1}: ")
    doc_n = doc_n.strip()
    docs.append(doc_n)

print()
m_targets = int(input("Liczba zapytań do przetworzenia (m): "))
print()

target_words = []

for i in range(m_targets): 
    m_targets = input(f"Wprowadź jednowyrazowe zapytanie {i+1}: ")
    m_targets = m_targets.strip()
    target_words.append(m_targets)

print()
print("Dokumenty do przetworzenia: ")
for doc in docs: 
    print(doc)

print()
print("Zapytania do przetworzenia: ")
for target_word in target_words: 
    print(target_word)

docs_without_punctuation = [doc.translate(str.maketrans('', '', string.punctuation)) for doc in docs]
docs_splitted = [[word for word in doc.lower().split()] for doc in docs_without_punctuation] 

word_counts = []

for doc_splitted in docs_splitted:
    counts = {}
    for target_word in target_words: 
        counts[target_word] = doc_splitted.count(target_word)

    word_counts.append(counts)

result = []

for target_word in target_words:
    word_list = [(i, counts.get(target_word, 0)) for i, counts in enumerate(word_counts)] # get index and word count
    sorted_word_list = sorted(word_list, key = lambda x: x[1], reverse = True) # sort by word count
    result_for_target = [i for i, count in sorted_word_list if count > 0] # create a list of indexes
    result.append(result_for_target)

print()
for i in result:
    print(i)