# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import glob
import os

def load_input(input_directory):
    """Load text files in 'input_directory/'"""

    files = glob.glob(f"{input_directory}/*")
    dataframes = [
        pd.read_csv(
            file,
            header=None,
            delimiter="\t",
            names=["phrase","sentiment"],
            index_col=None,
        )
        for file in files
    ]

    dataframe = pd.concat(dataframes, ignore_index=True)

    dataframe["target"] = input_directory.split("/")[3]

    return dataframe

def save_output(dataframe1, dataframe2, output_directory, output_name1, output_name2):
    """Save output to a file."""

    if os.path.exists(output_directory):
        files = glob.glob(f"{output_directory}/*")
        for file in files:
            os.remove(file)
        os.rmdir(output_directory)

    os.makedirs(output_directory)

    dataframe1.to_csv(
        f"{output_directory}/{output_name1}",
        sep=",",
        index=False,
        header=True,
    )
    dataframe2.to_csv(
        f"{output_directory}/{output_name2}",
        sep=",",
        index=False,
        header=True,
    )




def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    train_negative = load_input("files/input/train/negative")
    train_positive = load_input("files/input/train/positive")
    train_neutral = load_input("files/input/train/neutral")

    test_negative = load_input("files/input/test/negative")
    test_positive = load_input("files/input/test/positive")
    test_neutral = load_input("files/input/test/neutral")

    df_train = pd.concat([train_negative,train_neutral,train_positive], ignore_index=True)
    df_test = pd.concat([test_negative,test_neutral,test_positive],ignore_index=True)

    save_output(df_train, df_test, "files/output", "train_dataset.csv", "test_dataset.csv")
    return

pregunta_01()

train_dataset = pd.read_csv("files/output/train_dataset.csv")

assert "phrase" in train_dataset.columns
assert "target" in train_dataset.columns





    


