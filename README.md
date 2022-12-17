
# Reciept Digitization

# 1. Methodology 


![image](https://user-images.githubusercontent.com/55930740/208228572-31e89359-4202-44f1-9d2e-fc31ded0900d.png)

![image](https://user-images.githubusercontent.com/55930740/208228637-4c7141ce-c8df-4d39-9e7a-8bab6356ff0c.png)



# 2. Description

One of the biggest problems with the standard approach is the lack of generalization. Rule based approaches cannot generalize and new rules need to be written for any new template. Also any changes or variations in an existing template need to be accounted for too.

A Deep Learning approach will be able to learn these rules, and will be able to generalize across different layouts easily, provided we have them in our training dataset.

The proposed method is evaluated on ICDAR 2019 robust reading challenge on SROIE dataset and is also on a self-built dataset with 3 types of scanned document images.

The ICDAR 2019 SROIE data set is used which  contains 1000 whole scanned receipt images. Each receipt image contains around about four key text fields, such as goods name, unit price, date, and total cost. The text annotated in the dataset mainly consists of digits and English characters.

The self-built dataset contains 4, 484 annotated scanned Spanish receipt documents, including taxi receipts, meals entertainment (ME) receipts, and hotel receipts, with 9 different key information classes.


Results

The overall performance is evaluated using average precision (AP -  and measured in terms of per-class accuracy across the 9 classes,.) and soft average precision (softAP) where the prediction of a key information class is determined as correct if positive ground truths are correctly predicted even if some false positives are included in the final prediction.  joint analysis of AP and softAP provides a better understanding of the model performance.

![image](https://user-images.githubusercontent.com/55930740/208228652-fc8d245c-c19b-4b87-b058-9f76d7186d92.png)



# 3. Input/Output


![image](https://user-images.githubusercontent.com/55930740/208228879-6c95e944-5378-4db5-9c92-fee332d6ad6f.png)

Input is the raw bill image and output is the json which contains the particular fields

# 4. Live Link 

http://ishavgupta1234.pythonanywhere.com/

# 5. Screenshot of the interface

![image](https://user-images.githubusercontent.com/55930740/208229045-5b18adc0-bd5d-4336-8b58-7031185970fe.png)

![image](https://user-images.githubusercontent.com/55930740/208229064-8460b6f6-4b1a-43d9-8ef9-5e427023e8fd.png)

![image](https://user-images.githubusercontent.com/55930740/208229087-6d896cfd-12db-4497-b2b1-763dedbc9b80.png)

![image](https://user-images.githubusercontent.com/55930740/208229098-fad2c03b-d5c5-4af1-9ed8-9904561d5f96.png)

