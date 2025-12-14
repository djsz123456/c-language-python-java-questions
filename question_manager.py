import json
import os

class QuestionManager:
    def __init__(self, file_path='data/questions.json'):
        """
        初始化题库管理器
        :param file_path: 题库JSON文件路径
        """
        self.file_path = file_path
        self.questions = self.load_questions()
    
    def load_questions(self):
        """
        从JSON文件加载题目数据
        :return: 题目列表
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"文件 {self.file_path} 不存在，将创建新的题库文件。")
            return []
        except json.JSONDecodeError:
            print(f"文件 {self.file_path} 格式错误，将重新创建。")
            return []
    
    def save_questions(self):
        """
        保存题目数据到JSON文件
        """
        # 确保目录存在
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.questions, f, ensure_ascii=False, indent=2)
        print(f"题库已保存到 {self.file_path}")
    
    def get_next_id(self):
        """
        获取下一个可用的题目ID
        :return: 下一个ID
        """
        if not self.questions:
            return 1
        return max(q['id'] for q in self.questions) + 1
    
    def add_question(self, subject, question_type, question_content, answer, options=None, explanation=None):
        """
        添加新题目
        :param subject: 科目（如C++、Python、Java）
        :param question_type: 题型（选择题、填空题、编程题）
        :param question_content: 题目内容
        :param answer: 答案
        :param options: 选项列表（仅选择题需要）
        :param explanation: 解析（可选）
        :return: 添加的题目
        """
        new_question = {
            'id': self.get_next_id(),
            'subject': subject,
            'type': question_type,
            'question': question_content,
            'answer': answer
        }
        
        if question_type == '选择题' and options:
            new_question['options'] = options
        
        if explanation:
            new_question['explanation'] = explanation
        
        self.questions.append(new_question)
        self.save_questions()
        print(f"已添加新题目（ID: {new_question['id']}）")
        return new_question
    
    def get_question(self, question_id):
        """
        根据ID获取题目
        :param question_id: 题目ID
        :return: 题目字典或None
        """
        for q in self.questions:
            if q['id'] == question_id:
                return q
        return None
    
    def update_question(self, question_id, subject=None, question_type=None, question_content=None, 
                        answer=None, options=None, explanation=None):
        """
        更新题目信息
        :param question_id: 题目ID
        :param subject: 科目（可选）
        :param question_type: 题型（可选）
        :param question_content: 题目内容（可选）
        :param answer: 答案（可选）
        :param options: 选项列表（可选）
        :param explanation: 解析（可选）
        :return: 更新后的题目或None
        """
        question = self.get_question(question_id)
        if not question:
            print(f"未找到ID为 {question_id} 的题目")
            return None
        
        if subject:
            question['subject'] = subject
        if question_type:
            question['type'] = question_type
        if question_content:
            question['question'] = question_content
        if answer:
            question['answer'] = answer
        if options:
            question['options'] = options
        if explanation is not None:
            if explanation:
                question['explanation'] = explanation
            elif 'explanation' in question:
                del question['explanation']
        
        # 如果不是选择题，移除options字段
        if question.get('type') != '选择题' and 'options' in question:
            del question['options']
        
        self.save_questions()
        print(f"已更新题目（ID: {question_id}）")
        return question
    
    def delete_question(self, question_id):
        """
        删除题目
        :param question_id: 题目ID
        :return: 是否删除成功
        """
        question = self.get_question(question_id)
        if not question:
            print(f"未找到ID为 {question_id} 的题目")
            return False
        
        self.questions.remove(question)
        self.save_questions()
        print(f"已删除题目（ID: {question_id}）")
        return True
    
    def list_questions(self, subject=None, question_type=None):
        """
        列出题目
        :param subject: 科目筛选（可选）
        :param question_type: 题型筛选（可选）
        :return: 筛选后的题目列表
        """
        filtered = self.questions
        
        if subject:
            filtered = [q for q in filtered if q['subject'] == subject]
        
        if question_type:
            filtered = [q for q in filtered if q['type'] == question_type]
        
        return filtered
    
    def count_questions(self, subject=None, question_type=None):
        """
        统计题目数量
        :param subject: 科目筛选（可选）
        :param question_type: 题型筛选（可选）
        :return: 题目数量
        """
        return len(self.list_questions(subject, question_type))

# 使用示例
if __name__ == "__main__":
    # 创建题库管理器实例
    manager = QuestionManager()
    
    # 示例1：添加选择题
    manager.add_question(
        subject="Python",
        question_type="选择题",
        question_content="Python中用于遍历列表的循环结构是？",
        options=["for...in", "while", "foreach", "loop"],
        answer="for...in",
        explanation="Python使用for...in循环遍历列表等可迭代对象。"
    )
    
    # 示例2：添加填空题
    manager.add_question(
        subject="C++",
        question_type="填空题",
        question_content="C++中用于释放动态分配内存的运算符是？",
        answer="delete",
        explanation="C++使用delete运算符释放new分配的内存。"
    )
    
    # 示例3：统计题目数量
    print(f"\n总题目数: {manager.count_questions()}")
    print(f"Python题目数: {manager.count_questions(subject='Python')}")
    print(f"选择题数量: {manager.count_questions(question_type='选择题')}")
    
    # 示例4：列出所有题目
    print("\n所有题目：")
    for q in manager.list_questions():
        print(f"ID: {q['id']}, 科目: {q['subject']}, 题型: {q['type']}, 题目: {q['question']}")
