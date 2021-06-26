FAKEducation
------------
With the onset of global pandemic, it has been found that online learning is not easy _([ref](https://www.acetutoring.com/blogs/2020/9/17/battling-against-student-attention-span-in-online-learning#:~:text=Maintain%20Eye%20Contact.,when%20listening%20to%20online%20lessons.&text=Ask%20questions%20at%20the%20end.))_. It is also known that videos work better than text _([ref](http://wondermouse.us/blog-post/blog-test-1/))_. Hence I am trying to create video out of boring text, which will help people to be more attentive. It is an honest effort to make studies easier. Also it has been a constant complain in rural areas that video-conference based education is not possible. With the help of FAKEducation, one can create videos simply by their picture and the text/audio they want to use. It bridges the technological gap between non-techosavvy people and the latest technology. It makes learning easier by generating videos for text/audio content. We use deepfakes to generate video for the given content and is as simple as drag and drop for conversion. It also makes learning fun for kids, where their fav animated characters can teach them imp. topic just a mouseclick of efforts away. All-in-all FAKEducation tackles the issues with online education in a fun and smart way! It is easily reproducible and can reach people in all corners of the world!

Note : _Deep Fake framework implemented for [Paper](http://arxiv.org/abs/2008.10010)_

Implementation
--------------
You can easily host/implement the solution as shown in [colab](https://colab.research.google.com/drive/1j8nrSvUmMNWnt--ArEBSWf74twX5PGGp?usp=sharing). It is adviced to use colab because of easily available gpu units!


Prerequisites
-------------
- `Python 3.6` 
- ffmpeg: `sudo apt-get install ffmpeg`
- Install necessary packages using `pip install -r requirements.txt`. Alternatively, instructions for using a docker image is provided [here](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668). Have a look at [this comment](https://github.com/Rudrabha/Wav2Lip/issues/131#issuecomment-725478562) and comment on [the gist](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668) if you encounter any issues. 
- Face detection [pre-trained model](https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth) should be downloaded to `face_detection/detection/sfd/s3fd.pth`. Alternative [link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/prajwal_k_research_iiit_ac_in/EZsy6qWuivtDnANIG73iHjIBjMSoojcIV0NULXV-yiuiIg?e=qTasa8) if the above does not work.

Getting the weights
----------
| Model  | Description |  Link to the model | 
| :-------------: | :---------------: | :---------------: |
| Wav2Lip  | Highly accurate lip-sync | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZg80f7V9jtMfbNDaQ?e=TBFBVW)  |
| Wav2Lip + GAN  | Slightly inferior lip-sync, but better visual quality | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW) |
| Expert Discriminator  | Weights of the expert discriminator | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EQRvmiZg-HRAjvI6zqN9eTEBP74KefynCwPWVmF57l-AYA?e=ZRPHKP) |

How to run
------------
- Simply run python app.py
- It is recommended to have a system with GPU
- Can easily be run on colab and is actually easier that way. All you need is a weight file in your google drive. The rest of it can be used similar to the one [here](./FakeEducation.ipynb)


Acknowledgements
----------
Parts of the code structure is inspired by this [TTS repository](https://github.com/r9y9/deepvoice3_pytorch). We thank the author for this wonderful code. The code for Face Detection has been taken from the [face_alignment](https://github.com/1adrianb/face-alignment) repository. We thank the authors for releasing their code and models. We thank [zabique](https://github.com/zabique) for the tutorial collab notebook.
