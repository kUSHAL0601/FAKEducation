FAKEducate
----------
To tackle increased  issues with attention span in the online era, it is an honest effort to make studies easier. It bridges the technological gap between non-techosavvy people and the latest technology. It makes learning easier by generating videos for text/audio content. We use deepfakes to generate video for the given content and is as simple as drag and drop for conversion.
_Deep Fake framework implemented for [Paper](http://arxiv.org/abs/2008.10010)_

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


Acknowledgements
----------
Parts of the code structure is inspired by this [TTS repository](https://github.com/r9y9/deepvoice3_pytorch). We thank the author for this wonderful code. The code for Face Detection has been taken from the [face_alignment](https://github.com/1adrianb/face-alignment) repository. We thank the authors for releasing their code and models. We thank [zabique](https://github.com/zabique) for the tutorial collab notebook.
