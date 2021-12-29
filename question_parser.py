class QuestionPaser:

    '''构建实体节点'''
    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    '''解析主函数'''
    def parser_main(self, res_classify):
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            if question_type == 'disease_symptom':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'symptom_disease':
                sql = self.sql_transfer(question_type, entity_dict.get('symptom'))

            elif question_type == 'disease_cause':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_acompany':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_include':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_not_food':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_do_food':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_drug':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'drug_disease':
                sql = self.sql_transfer(question_type, entity_dict.get('drug'))

            elif question_type == 'disease_check':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))


            elif question_type == 'disease_prevent':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))


            elif question_type == 'disease_cureway':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_department':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_easyget':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_desc':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_hospital':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_article':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'disease_part':
                sql = self.sql_transfer(question_type, entity_dict.get('disease'))

            elif question_type == 'cure_drug':
                sql = self.sql_transfer(question_type, entity_dict.get('cure'))

            elif question_type == 'check_department':
                sql = self.sql_transfer(question_type, entity_dict.get('check'))

            elif question_type == 'check_part':
                sql = self.sql_transfer(question_type, entity_dict.get('check'))

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    '''针对不同的问题，分开进行处理'''
    def sql_transfer(self, question_type, entities):
        if not entities:
            return []

        # 查询语句
        sql = []
        # 查询疾病的原因
        if question_type == 'disease_cause':
            sql = ["MATCH (m:Disease)-[r:result_from]->(n:Cause) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病的防御措施
        elif question_type == 'disease_prevent':
            sql = ["MATCH (m:Disease)-[r:prevent_way]->(n:Prevention) where m.name = '{0}' return m.name, r.name, " \
                   "n.name".format(i) for i in entities]

        # 查询疾病包含的种类
        elif question_type == 'disease_include':
            sql = ["MATCH (m:Disease)-[r:include]->(n:Disease) where m.name = '{0}' return m.name, r.name, " \
               "n.name".format(i) for i in entities]

        # 查询疾病的治疗方式
        elif question_type == 'disease_cureway':
            sql = ["MATCH (m:Disease)-[r:treatment]->(n:Cure) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病的易发人群
        elif question_type == 'disease_easyget':
            sql = ["MATCH (m:Disease)-[r:easy_to_have]->(n:Crowd) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病的相关介绍
        elif question_type == 'disease_desc':
            sql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.description".format(i) for i in entities]

        # 查询疾病有哪些症状
        elif question_type == 'disease_symptom':
            sql = ["MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询症状会导致哪些疾病
        elif question_type == 'symptom_disease':
            sql = ["MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病的并发症
        elif question_type == 'disease_acompany':
            sql = ["MATCH (m:Disease)-[r:is_complicated]->(n:Disease) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病的忌口
        elif question_type == 'disease_not_food':
            sql = ["MATCH (m:Disease)-[r:no_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病建议吃的东西
        elif question_type == 'disease_do_food':
            sql = ["MATCH (m:Disease)-[r:do_not_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病常用药品
        elif question_type == 'disease_drug':
            sql = ["MATCH (m:Disease)-[r:take_medicine]->(n:Drug) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询治疗方式所用药品
        elif question_type == 'cure_drug':
            sql = ["MATCH (m:Cure)-[r:take_medicine]->(n:Drug) where m.name = '{0}' return m.name, r.name, n.name".format(
                i) for i in entities]


        # 已知药品查询能够治疗的疾病
        elif question_type == 'drug_disease':
            sql = ["MATCH (m:Disease)-[r:take_medicine]->(n:Drug) where n.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病应该进行的检查
        elif question_type == 'disease_check':
            sql = ["MATCH (m:Disease)-[r:need_check]->(n:Check) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询疾病所在的部门
        elif question_type == 'disease_department':
            sql = ["MATCH (m:Disease)-[r:belong_to]->(n:Department) where m.name = '{0}' return m.name, r.name, n.name".format(i) for i in entities]

        # 查询检查所在的部门
        elif question_type == 'check_department':
            sql = ["MATCH (m:Check)-[r:belong_to]->(n:Department) where m.name = '{0}' return m.name, r.name, n.name".format(
                i) for i in entities]

        # 查询疾病发生部位
        elif question_type == 'disease_part':
            sql = ["MATCH (m:Disease)-[r:happened]->(n:Part) where m.name = '{0}' return m.name, r.name, n.name".format(
                i) for i in entities]

        # 查询检查的部位
        elif question_type == 'check_part':
            sql = ["MATCH (m:Check)-[r:check_on]->(n:Part) where m.name = '{0}' return m.name, r.name, n.name".format(
            i) for i in entities]

        # 查询看病推荐的医院
        elif question_type == 'disease_hospital':
            sql = ["MATCH (m:Disease)-[r:recommand_hospital]->(n:Hospital) where m.name = '{0}' return m.name, " \
                   "r.name, n.name".format(i) for i in entities]

        # 查询看病推荐的医院
        elif question_type == 'disease_article':
            sql = ["MATCH (m:Disease)-[r:related_article]->(n:Article) where m.name = '{0}' return m.name, " \
                   "r.name, n.name".format(i) for i in entities]

        return sql



if __name__ == '__main__':
    handler = QuestionPaser()
