from flask import Flask, request, send_from_directory, redirect, render_template, flash, url_for, jsonify, \
    make_response, abort
from cornell_glove_predict import CornellWordGloveChatBot

app = Flask(__name__)
app.config.from_object(__name__) 


app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


cornell_word_glove_chat_bot = CornellWordGloveChatBot()

cornell_word_glove_chat_bot_conversations = []

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cornell_word_glove_reply', methods=['POST', 'GET'])
def cornell_word_glove_reply():
    if request.method == 'POST':
        if 'sentence' not in request.form:
            flash('No sentence post')
            redirect(request.url)
        elif request.form['sentence'] == '':
            flash('No sentence')
            redirect(request.url)
        else:
            sent = request.form['sentence']
            cornell_word_glove_chat_bot_conversations.append('YOU: ' + sent)
            reply = cornell_word_glove_chat_bot.reply(sent)
            cornell_word_glove_chat_bot_conversations.append('BOT: ' + reply)
    return render_template('cornell_word_glove_reply.html', conversations=cornell_word_glove_chat_bot_conversations)


@app.route('/chatbot_reply', methods=['POST', 'GET'])
def chatbot_reply():
    if request.method == 'POST':
        if not request.json or 'sentence' not in request.json or 'level' not in request.json or 'dialogs' not in request.json:
            abort(400)
        sentence = request.json['sentence']
        level = request.json['level']
        dialogs = request.json['dialogs']
    else:
        sentence = request.args.get('sentence')
        level = request.args.get('level')
        dialogs = request.args.get('dialogs')

    target_text = sentence
    if level == 'char' and dialogs == 'cornell':
        target_text = cornell_char_chat_bot.reply(sentence)
    elif level == 'word' and dialogs == 'cornell':
        target_text = cornell_word_chat_bot.reply(sentence)
    elif level == 'word-glove' and dialogs == 'cornell':
        target_text = cornell_word_glove_chat_bot.reply(sentence)
    return jsonify({
        'sentence': sentence,
        'reply': target_text,
        'dialogs': dialogs,
        'level': level
    })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    cornell_word_glove_chat_bot.test_run()
    app.secret_key = 'super secret key'
    app.run(debug=True)

if __name__ == '__main__':
    main()
