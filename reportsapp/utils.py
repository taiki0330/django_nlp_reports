def process_text(text):

    import re

    # with open("/Users/matsuzakidaiki/anaconda3/envs/django_nlp_env/reportsproject/reportsapp/reports/genba.txt", mode="r", encoding="utf-8") as f:  # ファイルの読み込み
    #     text_original = f.read()
    #     print(text_original)

    novels = ["/Users/matsuzakidaiki/anaconda3/envs/django_nlp_env/reportsproject/reportsapp/reports/genba.txt", "/Users/matsuzakidaiki/anaconda3/envs/django_nlp_env/reportsproject/reportsapp/reports/saigen.txt"]



    text = ""
    for novel in novels:
        with open(novel, mode="r", encoding="utf-8") as f:  # ファイルの読み込み
            text_novel = f.read()
        text_novel = re.sub("《[^》]+》", "", text_novel)  # ルビの削除
        text_novel = re.sub("［[^］]+］", "", text_novel)  # 読みの注意の削除
        text_novel = re.sub("〔[^〕]+〕", "", text_novel)  # 読みの注意の削除
        text_novel = re.sub("[ 　\n「」『』（）｜※＊…]", "", text_novel)  # 全角半角スペース、改行、その他記号の削除
        text += text_novel

    print("文字数:", len(text))
    print(text)

    from pykakasi import kakasi

    seperator = "。"  # 。をセパレータに指定
    sentence_list = text.split(seperator)  # セパレーターを使って文章をリストに分割する
    sentence_list.pop() # 最後の要素は空の文字列になるので、削除
    sentence_list = [x+seperator for x in sentence_list]  # 文章の最後に。を追加

    kakasi = kakasi()
    kakasi.setMode("J", "H")  # J(漢字) からH(ひらがな)へ
    conv = kakasi.getConverter()
    for sentence in sentence_list:
        print(sentence)
        print(conv.do(sentence))
        print()
        
        
    n_rnn = 10  # 時系列の数
    batch_size = 128
    epochs = 2
    n_mid = 256  # 中間層のニューロン数


    import numpy as np

    # インデックスと文字で辞書を作成
    chars = sorted(list(set(text)))  # setで文字の重複をなくし、各文字をリストに格納する
    print("文字数（重複無し）", len(chars))
    char_indices = {}  # 文字がキーでインデックスが値
    for i, char in enumerate(chars):
        char_indices[char] = i
    indices_char = {}  # インデックスがキーで文字が値
    for i, char in enumerate(chars):
        indices_char[i] = char
    
    # 時系列データと、それから予測すべき文字を取り出します
    time_chars = []
    next_chars = []
    for i in range(0, len(text) - n_rnn):
        time_chars.append(text[i: i + n_rnn])
        next_chars.append(text[i + n_rnn])
    
        # 入力と正解をone-hot表現で表します
    x = np.zeros((len(time_chars), n_rnn, len(chars)), dtype=np.bool_)
    t = np.zeros((len(time_chars), len(chars)), dtype=np.bool_)
    for i, t_cs in enumerate(time_chars):
        t[i, char_indices[next_chars[i]]] = 1  # 正解をone-hot表現で表す
        for j, char in enumerate(t_cs):
            x[i, j, char_indices[char]] = 1  # 入力をone-hot表現で表す
            
    print("xの形状", x.shape)
    print("tの形状", t.shape)


    from keras.models import Sequential
    from keras.layers import Dense, LSTM

    model_lstm = Sequential()
    model_lstm.add(LSTM(n_mid, input_shape=(n_rnn, len(chars))))
    model_lstm.add(Dense(len(chars), activation="softmax"))
    model_lstm.compile(loss='categorical_crossentropy', optimizer="adam")
    print(model_lstm.summary())


    from keras.callbacks import LambdaCallback
    
    def on_epoch_end(epoch, logs):
        print("エポック: ", epoch)

        beta = 5  # 確率分布を調整する定数
        prev_text = text[0:n_rnn]  # 入力に使う文字
        created_text = prev_text  # 生成されるテキスト
        
        print("シード: ", created_text)

        for i in range(400):
            # 入力をone-hot表現に
            x_pred = np.zeros((1, n_rnn, len(chars)))
            for j, char in enumerate(prev_text):
                x_pred[0, j, char_indices[char]] = 1
            
            # 予測を行い、次の文字を得る
            y = model.predict(x_pred)
            p_power = y[0] ** beta  # 確率分布の調整
            next_index = np.random.choice(len(p_power), p=p_power/np.sum(p_power))        
            next_char = indices_char[next_index]

            created_text += next_char
            prev_text = prev_text[1:] + next_char

        print(created_text)
        print()

    # エポック終了後に実行される関数を設定
    epock_end_callback= LambdaCallback(on_epoch_end=on_epoch_end)


    model = model_lstm
    history_lstm = model_lstm.fit(x, t,
                        batch_size=batch_size,
                        epochs=epochs,
                        callbacks=[epock_end_callback])


    from keras.layers import GRU

    model_gru = Sequential()
    model_gru.add(GRU(n_mid, input_shape=(n_rnn, len(chars))))
    model_gru.add(Dense(len(chars), activation="softmax"))
    model_gru.compile(loss='categorical_crossentropy', optimizer="adam")
    print(model_gru.summary())

    model = model_gru
    history_gru = model_gru.fit(x, t,
                        batch_size=batch_size,
                        epochs=epochs,
                        callbacks=[epock_end_callback])

    import matplotlib.pyplot as plt

    loss_lstm = history_lstm.history['loss']
    loss_gru = history_gru.history['loss']

    plt.plot(np.arange(len(loss_lstm)), loss_lstm, label="LSTM")
    plt.plot(np.arange(len(loss_gru)), loss_gru, label="GRU")
    plt.legend()
    plt.show()