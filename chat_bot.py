

from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '我还没有这个记录哦！或者您可以精确疾病的用词，如神经性厌食症、小儿厌食症、青春期厌食症'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    print('助理:您好，我是厌食症知识助理，可以询问我有关于厌食症的一些内容！')
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('助理:', answer)

