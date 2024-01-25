import streamlit as st
from GameManager import GameManager
from ReadJSONFile import ReadJSONFile
import time
import uuid



class FrontEnd:

    def __init__(self):
        self.game_manager = GameManager()
        self.number_question = 0
        self.questions_container = None
        self.question_empty = None

    def init_front(self):
        st.title("Bem vindo ao jogo da perguntas!")
        container = st.empty()
        file = container.file_uploader("Para começar entre com um arquivo JSON com as perguntas", type=["txt"], accept_multiple_files=False)

        if file is not None:
            file = ReadJSONFile.read_json(file)
            self.game_manager.config_game(file["perguntas"], self)
            container.empty()
            self.init_game()

    def init_game(self):
        self.question_empty = st.empty()
        self.questions_container = self.question_empty.container()
        self.next_question()

    def next_question(self):
        self.question_empty.empty()
        self.questions_container = self.question_empty.container(border=True)
        question = self.game_manager.return_question(self.number_question)
        if question == -1:
            pass  # fim do jogo
        self.print_question(question)
        self.number_question += 1

    def print_question(self, question):
        # interfaces
        self.questions_container.title(("Pergunta número " + str(self.number_question+1)))
        self.questions_container.markdown(question['texto'])

        if question["tipo"] == "aberta":
            self.print_question_open(question)
        elif question["tipo"] == "verdadeiro_falso":
            self.print_question_true_or_false(question)
        elif question["tipo"] == "multipla_escolha":
            self.print_question_closed(question)

    def print_question_open(self, question):
        texto_digitado = self.questions_container.text_input("Digite a resposta aqui: ")
        submit_button = self.questions_container.button("Submeter resposta", use_container_width=True)
        if submit_button:
            st.write("proximas pergunta")
            self.game_manager.update_score(self.number_question, texto_digitado)
            self.next_question()

    def print_question_true_or_false(self, question):
        true_false = self.questions_container.radio("Marque uma alternativa", ("Verdadeiro", "Falso"))
        submit_button = self.questions_container.button("Submeter resposta")
        if submit_button:
            self.game_manager.update_score(self.number_question, true_false)
            self.next_question()

    def print_question_closed(self, question):
        pass
