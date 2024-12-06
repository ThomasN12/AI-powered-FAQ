from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import openai
from typing import List, Dict

class FAQGenerator:
    def __init__(self):
        # TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer
        # Converts text into numerical vectors by:
        # - Calculating how frequently terms appear in a document (TF)
        # - Weighing down common words that appear across many documents (IDF)
        # stop_words='english' removes common English words (a, the, is, etc.)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    def cluster_questions(self, questions: List[Dict]) -> List[List[Dict]]:
        texts = [q['title'] + ' ' + q.get('body', '') for q in questions]
        
        # Convert text to TF-IDF vectors
        # Each question becomes a numerical vector where each dimension
        # represents the TF-IDF score of a word in the corpus
        vectors = self.vectorizer.fit_transform(texts)
        
        # KMeans clustering groups similar questions based on their vector representations
        # Questions with similar word frequencies will be clustered together
        # An unsupervised learning approach to find natural groupings
        n_clusters = min(5, len(questions))  # Get 5 FAQs or less
        clustering = KMeans(n_clusters=n_clusters).fit(vectors)
        
        # Group questions by cluster label
        clusters = {}
        for idx, label in enumerate(clustering.labels_):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(questions[idx])
        
        return list(clusters.values())

    # def get_best_answer(self, cluster: List[Dict]) -> str:
    #     # Use the answer from the highest-scored post in cluster
    #     best_post = max(cluster, key=lambda x: x['score'])
    #     return best_post['answer']

    def generate_faq(self, questions: List[Dict]) -> List[Dict]:
        clusters = self.cluster_questions(questions)
        faqs = []
        
        for cluster in clusters:
            # answer = self.get_best_answer(cluster)
            main_question = cluster[0]
            # if main_question['title'] == "How can I create an virtual diskette with my files?":
            #     print(f"Question title: {main_question['title']}")
            #     print(f"Answer: {answer}")
            #     print(f"Cluster Answer: {main_question['answer']}")
            # print(f"Question title: {main_question['title']}")
            # print(f"Answer: {answer}")
            faqs.append({
                'question': main_question['title'],
                'question_body': main_question['body'],
                'answer': main_question['answer'],
                'related_questions': [q['title'] for q in cluster[1:]]
            })
        
        return faqs