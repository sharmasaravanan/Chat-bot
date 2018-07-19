# Chat-bot
1) Download the zip and unzip keep that folder as it is.
2) Install all the libraries by using the following commands 
          
                                    pip install -r install.txt
3) To train the chatbot,
      A) go to the folder chatbot into that chatbot train and run the following command to train    
 
                                    python3 cornell_glove_train.py
      B) once the training process is done you check the model files created in the model directory.
4) To predict or to chat with bot,
     A) Go to chatbot folder and open the terminal in that directory, run the following command 
                                    
                                    Python3 flaskr.py
     B) it will generate the link like the following 
                                  
                                    http://127.0.0.1:5000 
     C) click that link... which will be opened in the browser where you have to click the cornell link.
     D) Which will be redirected to the chatbot page where you can chat with that boy.
