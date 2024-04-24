import streamlit as st


# Função para converter o rating SUS em emojis
def sus_para_emojis(sus_score):
    if sus_score >= 85:
        return "🎉 Muito bom!"
    elif sus_score >= 70:
        return "😃 Bom"
    elif sus_score >= 50:
        return "😐 Regular"
    elif sus_score >= 35:
        return "😕 Ruim"
    else:
        return "😞 Muito ruim"

# Descrição do System Usability Scale (SUS)
descricao_sus = """
O System Usability Scale (SUS) é uma ferramenta amplamente utilizada para avaliar a usabilidade de sistemas, produtos e serviços. Foi desenvolvido por John Brooke em 1986 e desde então tem sido um instrumento popular para medir a percepção dos usuários sobre a facilidade de uso de um sistema.

O SUS consiste em uma escala de 10 itens, onde os usuários são solicitados a responder com uma pontuação de concordância em uma escala de cinco pontos (variando de "Discordo totalmente" a "Concordo totalmente"). Os itens avaliam diferentes aspectos da usabilidade, como facilidade de uso, eficiência, aprendizagem e satisfação geral do usuário.

A pontuação SUS é calculada somando as pontuações individuais de cada item, ajustando-as conforme necessário e multiplicando o total por 2,5 para obter uma pontuação final entre 0 e 100. Quanto maior a pontuação, melhor a usabilidade percebida do sistema.

Em resumo, o SUS fornece uma medida quantitativa da usabilidade percebida de um sistema, permitindo que os desenvolvedores identifiquem áreas de melhoria e avaliem o sucesso de intervenções de design.
"""

image = "like2.png"
st.image(image, caption='', use_column_width=True)

# Depoimento e avaliação SUS existentes
depoimento_existente = '"Visualmente feio, cores sem graça"'
depoimento_existente1 = '"Podemos dar mais a cara da Laniaq, avatar, cores, línguagem dos scripts"'
depoimento_existente2 = '"funcionalidade com o Slack ou Pipefy"'
depoimento_existente3 = '"Com relação as funcionalidade é possível modificar para ficar mais parecido com whatsapp possível.."'
depoimento_existente4 = '"Preciso entender e usar mais pra opinar mudanças"'

depoimento_existente5 = '"Com relação as funcionalidade é possível modificar para ficar mais parecido com whatsapp possível.. "'


sus_score_existente = 68
score_desempenho = 80
score_satisfação = 50


# Exibir a descrição do SUS
st.header("Descrição do System Usability Scale (SUS)")

st.write(descricao_sus)


st.header("Resultado - Usabilidade")



descricao_Resultado = 'Os resultados do teste System Usability Scale (SUS) fornecem uma medida quantitativa da usabilidade percebida de um sistema, produto ou serviço. A pontuação SUS é calculada a partir das respostas dos usuários a uma série de perguntas sobre a facilidade de uso, eficiência, aprendizagem e satisfação geral com o sistema.'


st.write( descricao_Resultado)


st.write('Resultado Geral: ' + sus_para_emojis(sus_score_existente))



st.header("Resultado - Desempenho")

descricao_resultado_desempenho = 'Os resultados de um teste de desempenho fornecem uma avaliação da capacidade de um sistema, aplicativo ou serviço de realizar tarefas específicas em um determinado contexto. Este tipo de teste mede diversos aspectos, como velocidade, eficiência, escalabilidade, estabilidade e confiabilidade do sistema.'


st.write('Resultado Geral: ' + sus_para_emojis(score_desempenho))

st.write(descricao_resultado_desempenho)



st.header("Resultado - Satisfação")

descricao_resultado_satisfacao = '"A avaliação da satisfação do usuário em uma pesquisa de usabilidade desempenha um papel fundamental na melhoria contínua de sistemas e produtos digitais. Através do entendimento das percepções e experiências dos usuários, é possível identificar áreas de sucesso e oportunidades de aprimoramento.'


st.write('Resultado Geral: ' + sus_para_emojis(score_satisfação))

st.write(descricao_resultado_desempenho)



# Exibir o depoimento e a avaliação SUS existentes
st.header("Sugestões dos Usuários")
st.write("Sugestões:")
st.write(depoimento_existente)
st.write(depoimento_existente1) 
st.write(depoimento_existente2)
st.write(depoimento_existente3)
st.write(depoimento_existente4)
st.write(depoimento_existente5)
