# RetrImage
![image](https://user-images.githubusercontent.com/92720531/171821185-e82b3c89-3fef-4782-8e5d-8788a89bca6b.png)
![image](https://user-images.githubusercontent.com/92720531/171821573-59f3217a-a45b-438f-a410-472da5c79253.png)
![image](https://user-images.githubusercontent.com/92720531/171821661-fc6f4ef1-7269-40ce-a4e2-33ad1fb5e696.png)
Due to recent development in technology, there is an increase in the usage of digital cameras, smartphone, and Internet. The shared and stored multimedia data are growing. Digital images constitute a major part of multimedia data. In last few years, the complexity of multimedia contents, especially the images, has grown exponentially, and on daily basis, more than millions of images are uploaded at different archives such as Twitter, Facebook, and Instagram. To search for a relevant image from an archive is a challenging problem. For this problem we can use content based image retrieval (CBIR) system.

CBIR is the process by which one searches for similar images according to the content of the query image, such as color, texture, shape, and so forth

In CBIR, images are represented in the form of features that consists of numerical values. The research shows that there is a significant gap between image feature representation and human visual understanding.

The basic need for any image retrieval system is to search and sort similar images from the archive with minimum
Computational cost and more reliable result.  A machine learning algorithm can be applied by using training-testing. Machine learning is effectively increasing the quality of retrieval. Also we can use deep neural networks (DNN), which are able to generate better results at a high computational cost .
![image](https://user-images.githubusercontent.com/92720531/171822255-a0bc5719-e3a5-4eb3-a6f2-6bf6a01690d5.png)

![image](https://user-images.githubusercontent.com/92720531/171822308-e844b3fc-4ada-4028-b845-0368624ffb69.png)

<b>1.Feature extraction:</b> 
	As discussed earlier we can use colour, shape ,texture as features. In our we need to find similarity among the given images of various resolution and size. To convert image to feature vector we would have resolution*3(for rgb). This number is in millions and processing of data would be slow and is not the most convient way.
Therefore I am using here histogram of colors as feature vector which converts each image to 768 numbers. These numbers are the 256 shades of each RGB colour. Therefore irrespective of size or resolution we can compare images. We reduce the dimension of feature vector from millions to 768 for each image.
So our first step is to read the dataset , extract feature from images and store it in a file to the further process.

<b>2.Applying ML  :</b>
Now we have the list of features of images given in the dataset.
In CBIR we will be given an query image and then we have to show similar
images. To implement this we use nearest neighbour approach. For
nearest neighbour we use distance as factor to compute similarity. But
since we have feature vector which is a histogram we use chi squared
distance
![image](https://user-images.githubusercontent.com/92720531/171823039-d0ba46d6-1255-431c-a5bc-130e4fd4caa1.png)

For the given query and every other images in the dataset ,squared
distance is calculated. Then we sort the result as lowest values will
give more similar images , we give the limit to this as much we
require.We use K means clustering to cluster the images in group for
further result analysis

<h1>3.Obatining result : </h1><sr><br>
Now we have every
needed functions. We input query and we get similar
images with more similar in front of the list.<br>
Command line syntax:<br>
  <b>Step1:</b>python index.py<br>
dataset dataset index index.csv<br>
#Here dataset is the location of the images in our dataset
<br>#index.csv is the csv which will be created , it stores the feature vector<br>
<b>Step2:</b>python retrieve.py<br>
index index.csv query queries/0.jpg result_path dataset
<br>#here query stores location of our query image
<br>We use
Kmeans clustering to compare the result of retrieved image to find how much
our result was accurate, both precision and recall were calculated. Cluster from
Kmeans were compared in terms of original clusters.For this we ran query of each
image in dataset to get the report

![image](https://user-images.githubusercontent.com/92720531/171824043-5d5c7137-9496-49ee-bbfe-91ac347ca65b.png)
![image](https://user-images.githubusercontent.com/92720531/171824436-373525b5-c6d7-426d-94e8-3730307a6521.png)
![image](https://user-images.githubusercontent.com/92720531/171824568-2317468f-e093-4831-a0fd-9ea95c4a3af1.png)
![image](https://user-images.githubusercontent.com/92720531/171824588-f759ab19-da25-4249-a492-ec5cf5346896.png)
![image](https://user-images.githubusercontent.com/92720531/171824614-c629312f-b44b-432d-bce2-972a01c7ced4.png)
<h5>Average Recall=0.7406</h5>
<h5>Average Precision=0.8569</h5>
