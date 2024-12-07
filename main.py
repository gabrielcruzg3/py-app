from scripts.data_preprocessing import carregar_dados, preprocessar_dados, preprocessar_cursos
from app import app
import config

if __name__ == "__main__":
    # Pré-processar dados
    df = carregar_dados(config.PATH_MICRODADOS)
    # df = preprocessar_dados(df)
    # df.to_csv(config.PATH_CURSOS_PREPROCESSADOS, index=False)
    
    df = preprocessar_cursos(df)
    df.to_csv(config.PATH_CURSOS_PREPROCESSADOS, index=False)
    
    # Iniciar aplicação Flask
    app.run(debug=True)
