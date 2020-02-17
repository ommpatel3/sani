# Sani
> from *Sanitas* - Health in latin

Using Blockchain and Computer Vision technology to digitize crucial healthcare documents

## Completion List
*Computer Vision*
- [x] OpenCV & Tesseract: Optical Character Recognition
- [x] OHIP card recognition
- [x] mqtt publishing (sending data)
- [ ] generalize to various documents

*Blockchain*
- [x] React front-end
- [x] Blockstack authenticated login
- [x] mqtt subscription (recieving data) and display
- [ ] full Blockstack/Gaia Database integration

## Running Sani
**In bash**
1) Navigate to folder
  ```$ cd <insert path>```
2) Run the site
  ```$ npm run start```
3) Wait for the site to open
4) Complete Blockstack authentication/login
5) Wait for page to load (without data)
6) Run ID Scanner (orient OHIP card so that the Name and card number are within the boxes, then press spacebar to submit)
  ```$ python ID\ Scanner.py```

*Note: This is after having inserted mqtt broker link in both ```src/profile.js``` and ```ID Scanner.py```*
