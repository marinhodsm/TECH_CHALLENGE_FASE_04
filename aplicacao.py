# Aplicação Streamlit — Dashboard + Predição de Obesidade

# ==================================================
# BIBLIOTECAS
# ==================================================

import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title='Painel de Apoio à Prevenção da Obesidade',
    page_icon='📊',
    layout='wide'
)

# ==================================================
# CARREGAMENTO DO MODELO TREINADO
# ==================================================

modelo = joblib.load('modelo_obesidade.pkl')

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title('🏥 Painel de Apoio à Prevenção da Obesidade')

pagina = st.sidebar.radio(
    'Navegação',
    [
        'Visão Geral',
        'Fatores de Risco',
        'Hábitos Preventivos',
        'Predição Individual'
    ]
)

# ==================================================
# VISÃO GERAL
# ==================================================

if pagina == 'Visão Geral':

    st.title('🏥 Painel Inteligente de Apoio à Prevenção da Obesidade')

    st.markdown('---')

    st.markdown(
        '''
        Este painel foi desenvolvido para apoiar a identificação de fatores
        associados à obesidade e auxiliar ações de prevenção e promoção da saúde.

        A solução utiliza técnicas de Ciência de Dados e Machine Learning para
        analisar características comportamentais e corporais relacionadas aos
        diferentes níveis de obesidade.
        '''
    )

    st.markdown('---')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            '🤖 **MODELO UTILIZADO**',
            'XGBoost'
        )

    with col2:
        st.metric(
            '🎯 **ACURÁCIA OBTIDA**',
            '96,2%'
        )

    with col3:
        st.metric(
            '📊 **CLASSES PREVISTAS**',
            '7 níveis'
        )

    st.markdown('---')

    st.subheader('📋 Funcionalidades')

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            '''
            📊 **ANÁLISE DE FATORES ASSOCIADOS À OBESIDADE**

            Identificação das variáveis mais relevantes para a classificação
            dos níveis de obesidade.
            '''
        )

        st.info(
            '''
            ⚠️ **AVALIAÇÃO DE FATORES DE RISCO**

            Destaque para hábitos e comportamentos associados ao aumento
            da probabilidade de obesidade.
            '''
        )

    with col2:

        st.info(
            '''
            ❤️ **HÁBITOS PREVENTIVOS**

            Apresentação de práticas relacionadas à promoção da saúde
            e prevenção da obesidade.
            '''
        )

        st.info(
            '''
            🤖 **PREDIÇÃO INDIVIDUAL**

            Simulação personalizada do nível de obesidade com base
            nas características pessoais informadas pelo usuário.
            '''
        )

    st.markdown('---')

    st.subheader('🔎 Principais Achados')

    st.success(
        '''
        • Medidas corporais como peso e altura apresentaram forte influência
        na classificação dos níveis de obesidade.

        • Fatores comportamentais também demonstraram relevância,
        especialmente hábitos alimentares e padrões de consumo.

        • O modelo XGBoost apresentou o melhor desempenho entre os modelos avaliados.

        • Os resultados reforçam a importância de estratégias preventivas
        focadas em alimentação saudável e estilo de vida ativo.
        '''
    )

    st.caption(
        '''
        Este sistema possui finalidade educacional e de apoio à análise de dados.
        Os resultados não substituem avaliação médica ou diagnóstico profissional.
        '''
    )

# ==================================================
# FATORES DE RISCO
# ==================================================

elif pagina == 'Fatores de Risco':

    st.title('⚠️ Fatores de Risco')

    st.markdown('---')

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        '🍺 **CONSUMO DE ÁLCOOL**',
        'Alto Impacto'
    )

    col2.metric(
        '🍔 **ALIMENTAÇÃO**',
        'Alto Impacto'
    )

    col3.metric(
        '🚶 **SEDENTARISMO**',
        'Moderado'
    )

    col4.metric(
        '🚬 **CIGARRO**',
        'Baixo'
    )

    st.markdown('---')
    
    st.subheader('Principais Fatores Associados ao Aumento do Risco')

    col1, col2 = st.columns(2)

    with col1:

        st.warning(
            '''
            🍺 **CONSUMO DE ÁLCOOL**

            O consumo frequente de bebidas alcoólicas pode aumentar
            a ingestão calórica diária e favorecer o ganho de peso
            ao longo do tempo.
            '''
        )

        st.warning(
            '''
            🍔 **CONSUMO DE ALIMENTOS ALTAMENTE CALÓRICOS**

            O consumo frequente de alimentos ricos em gorduras,
            açúcares e ultraprocessados está associado ao ganho
            excessivo de peso.
            '''
        )

    with col2:

        st.warning(
            '''
            🍪 **LANCHES ENTRE REFEIÇÕES**

            O hábito frequente de consumir alimentos entre as
            refeições principais pode contribuir para o excesso
            de ingestão calórica.
            '''
        )

        st.warning(
            '''
            🚗 **SEDENTARISMO E DESLOCAMENTO**

            Meios de transporte mais ativos, como caminhar ou
            pedalar, contribuem para maior gasto energético
            diário quando comparados ao uso exclusivo de veículos.
            '''
        )

    st.markdown('---')

    st.subheader('Interpretação')
    
    st.info(
        '''
        Os resultados indicam que hábitos relacionados à alimentação,
        consumo de álcool e nível de atividade cotidiana estão entre os
        principais fatores associados aos diferentes níveis de obesidade.

        Embora características corporais como peso e altura tenham grande
        influência na classificação, fatores comportamentais representam
        oportunidades importantes para prevenção e promoção da saúde.
        '''
    )

# ==================================================
# HÁBITOS PREVENTIVOS
# ==================================================

elif pagina == 'Hábitos Preventivos':

    st.title('❤️ Hábitos Preventivos')

    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            '''
            🏃 **ATIVIDADE FÍSICA**

            Praticar exercícios regularmente contribui para o controle do peso corporal,
            melhora a saúde cardiovascular e reduz o risco de obesidade.
            '''
        )

        st.success(
            '''
            🥗 **ALIMENTAÇÃO BALANCEADA**

            Aumentar o consumo de vegetais e reduzir alimentos ultraprocessados
            está associado a melhores indicadores de saúde.
            '''
        )

    with col2:

        st.success(
            '''
            💧 **HIDRATAÇÃO**

            A ingestão adequada de água auxilia o funcionamento do organismo
            e favorece hábitos alimentares mais saudáveis.
            '''
        )

        st.success(
            '''
            😴 **ESTILO DE VIDA SAUDÁVEL**

            A combinação entre alimentação equilibrada, atividade física e
            monitoramento da saúde contribui para a prevenção da obesidade.
            '''
        )

    st.markdown('---')

    st.subheader('Interpretação')

    st.info(
        '''
        Os resultados obtidos indicam que hábitos relacionados à prática de atividade física,
        alimentação saudável e hidratação apresentam associação com menores níveis de obesidade.

        Embora fatores corporais como peso e altura sejam os mais influentes na classificação,
        os hábitos de vida continuam desempenhando papel importante na prevenção e no controle
        do excesso de peso.

        Dessa forma, estratégias de educação alimentar, incentivo à atividade física e promoção
        da saúde podem contribuir para a redução dos fatores de risco associados à obesidade.
        '''
    )

# ==================================================
# PREDIÇÃO INDIVIDUAL
# ==================================================

elif pagina == 'Predição Individual':

    st.title('📊 Predição Individual')

    st.markdown('---')

    st.markdown('''
    Para realizar sua predição individual, preencha o formulário abaixo com seus dados pessoais e clique no botão "Realizar Predição" ao final da página.
    ''')

    with st.form('form_obesity'):

        st.subheader('Formulário para Predição Individual')

        # ==============================================
        # DADOS PESSOAIS
        # ==============================================

        gender = st.selectbox(
            'Gênero',
            ['Feminino', 'Masculino']
        )

        age = st.number_input(
            'Idade',
            min_value=10,
            max_value=100
        )

        weight = st.number_input(
            'Peso (kg)',
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format='%.1f'
        )

        height = st.number_input(
            'Altura (m)',
            min_value=1.00,
            max_value=2.50,
            value=1.70,
            step=0.01,
            format='%.2f'
        )

        # ==============================================
        # HÁBITOS E COMPORTAMENTOS
        # ==============================================

        family_history = st.selectbox(
            'Possui histórico familiar de excesso de peso?',
            ['Sim', 'Não']
        )

        favc = st.selectbox(
            'Consume frequentemente alimentos muito calóricos?',
            ['Sim', 'Não']
        )

        fcvc = st.slider(
            "Frequência de consumo de vegetais nas refeições\n\n(1: raramente | 2: às vezes | 3: sempre)",
            min_value=1,
            max_value=3
        )

        ncp = st.slider(
            "Número de refeições principais por dia\n\n(1: uma refeição | 2: duas refeições | 3: três refeições | 4: quatro refeições ou mais)",
            min_value=1,
            max_value=4
        )

        caec = st.select_slider(
            "Tem hábito de comer lanches entre as refeições?",
            options=
            [
                "Não",
                "Às vezes",
                "Frequentemente",
                "Sempre"
            ]
        )

        smoke = st.selectbox(
            'Tem hábito de fumar?',
            ['Sim', 'Não']
        )

        ch2o = st.slider(
            "Consumo diário de água\n\n(1: < 1L | 2: 1–2L | 3: > 2L)",
            min_value=1,
            max_value=3
        )

        scc = st.selectbox(
            'Faz monitoramento de ingestão calórica diária?',
            ['Sim', 'Não']
        )

        faf = st.slider(
            "Frequência semanal de atividade física\n\n(0: nenhuma | 1: 1 a 2 vezes | 2: 3 a 4 vezes | 3: 5 vezes ou mais)",
            min_value=0,
            max_value=3
        )

        tue = st.slider(
            "Tempo diário usando dispositivos eletrônicos\n\n(0: 0 a 2 horas | 1: 3 a 5 horas | 2: 5 horas ou mais)",
            min_value=0,
            max_value=2
        )

        calc = st.select_slider(
            "Tem hábito de consumo de bebida alcoólica?",
            options=
            [
                "Não",
                "Às vezes",
                "Frequentemente",
                "Sempre"
            ]
        )

        mtrans = st.selectbox(
            'Meio de transporte habitual',
            [
                "Carro",
                "Moto",
                "Bicicleta",
                "Transporte público",
                "A pé"
            ]
        )

        # ==============================================
        # BOTÃO
        # ==============================================

        col1, col2, col3 = st.columns([1, 1, 1])

        with col2:
            submit = st.form_submit_button(
                'Realizar Predição'
            )

    # ==============================================
    # RESULTADO
    # ==============================================

    if submit:

        dados = pd.DataFrame({

            'Gender': [gender],
            'Age': [age],
            'Weight': [weight],
            'Height': [height],
            'family_history': [family_history],
            'FAVC': [favc],
            'FCVC': [fcvc],
            'NCP': [ncp],
            'CAEC': [caec],
            'SMOKE': [smoke],
            'CH2O': [ch2o],
            'SCC': [scc],
            'FAF': [faf],
            'TUE': [tue],
            'CALC': [calc],
            'MTRANS': [mtrans]
        })

        predicao = modelo.predict(dados)

        resultado_modelo = int(predicao[0])

        # ORDEM ALFABÉTICA DO MODELO MANTIDA
        traducao = {
            0: '🔹 Peso Abaixo do Normal',
            1: '✅ Peso Normal',
            5: '🟡 Sobrepeso Nível I',
            6: '🟠 Sobrepeso Nível II',
            2: '⚠️ Obesidade Grau I',
            3: '🚨 Obesidade Grau II',
            4: '🔴 Obesidade Grau III'
        }

        resultado = traducao[resultado_modelo]

        st.markdown('---')

        st.subheader('Resultado da Predição')

        st.success(resultado)

        mensagens = {

        0:
            '''
            O resultado indica peso abaixo do intervalo considerado adequado.
            
            Recomenda-se avaliação nutricional para verificar possíveis deficiências
            alimentares, condições metabólicas ou outros fatores que possam estar
            influenciando o peso corporal.
            ''',

        1:
            '''
            O resultado indica peso dentro da faixa considerada saudável.
            
            Recomenda-se a manutenção dos hábitos atuais, incluindo alimentação
            equilibrada, prática regular de atividade física e acompanhamento
            periódico da saúde.
            ''',

        5:
            '''
            O resultado sugere presença de excesso de peso inicial.
            
            Pequenas mudanças nos hábitos alimentares e aumento da atividade física
            podem contribuir significativamente para o controle do peso e prevenção
            da progressão para níveis mais elevados de obesidade.
            ''',

        6:
            '''
            O resultado indica um nível mais avançado de excesso de peso.
            
            Recomenda-se atenção aos hábitos alimentares, prática regular de
            exercícios físicos e acompanhamento profissional para evitar o avanço
            do quadro.
            ''',

        2:
            '''
            O resultado sugere obesidade em estágio inicial.
            
            A adoção de um plano estruturado de alimentação saudável e atividade
            física pode auxiliar na redução dos riscos associados ao excesso de peso.
            A avaliação médica também é recomendada.
            ''',

        3:
            '''
            O resultado indica obesidade moderada.
            
            Nessa condição, aumentam os riscos para doenças cardiovasculares,
            diabetes tipo 2 e outras complicações. Recomenda-se acompanhamento
            multiprofissional envolvendo médico e nutricionista.
            ''',

        4:
            '''
            O resultado indica obesidade grave.
            
            Este nível está associado a maior risco de complicações clínicas e
            redução da qualidade de vida. Recomenda-se avaliação médica
            especializada para definição das estratégias de tratamento mais
            adequadas.
            '''
        }

        st.info(mensagens[resultado_modelo])