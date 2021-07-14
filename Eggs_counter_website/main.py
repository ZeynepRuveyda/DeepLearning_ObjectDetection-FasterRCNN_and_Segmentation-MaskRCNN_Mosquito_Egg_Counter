import streamlit as st

st.set_page_config(layout="wide")
from PIL import Image, ImageOps
import os
import numpy as np
import time
import image_slicer
import detectron2
import torch
import cv2
from detectron2.utils.logger import setup_logger

setup_logger()

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor, DefaultTrainer, HookBase
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog, build_detection_test_loader
from detectron2.structures import BoxMode
from detectron2.utils.events import get_event_storage
from detectron2.evaluation import COCOEvaluator, inference_on_dataset


def predict(im):
    cfg = get_cfg()

    # Set Our Architecture & Weights

    model_path = "COCO-Detection/faster_rcnn_R_50_DC5_1x.yaml"

    cfg.merge_from_file(model_zoo.get_config_file(model_path))
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(model_path)
    if count_egg:
        if file_uploaded is None:

            st.write("Invalid command, please upload an image")
        else:
            cfg.MODEL.WEIGHTS = "/content/drive/MyDrive/model_final_51d356.pkl"

            # cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0
            predictor = DefaultPredictor(cfg)
            outputs = predictor(im)
            return len(outputs['instances'].pred_boxes)


@st.cache
def viso(outputs, im):
    visualizer = Visualizer(image,
                            metadata=train_metadata,
                            scale=1.0)

    visualizer = visualizer.draw_instance_predictions(outputs['instances'].to("cpu"))
    return visualizer.get_image()


st.write("# Welcome to Mosquitoes Eggs Detection and Counter ")
co1, co2, co3, co4, co5 = st.beta_columns([1, 1, 1, 1, 1])
co2.markdown(
    "![Alt Text](https://ww2.kqed.org/app/uploads/sites/35/2020/04/DL706_Aedes_aegypti_mosquito_lays_eggs1.gif)")
st.markdown("*(A female Aedes aegypti mosquito lays eggs on a glass surface at UC Davis. A. aegypti lay their eggs "
            "above the water line, rather than directly on the water's surface, as other mosquitoes do. (Josh "
            "Cassidy/KQED))*")
st.write("-----------")
st.sidebar.title("Upload Image and Count")
st.sidebar.write("-----------")
st.sidebar.write("**Usage of Sidebar** ")
st.sidebar.write("Upload image and it will read and will divide by 6 than will make invert. After it will show bbox "
                 "that you can see which eggs did not find than you can quick look add to additional eggs in the text "
                 "bar it will calculate total eggs predicted and by view.")

path = st.sidebar.text_input('Input your images path:')

file_uploaded = st.sidebar.file_uploader("Choose Image", type=["png", "jpg", "jpeg", "tif"])

if file_uploaded is not None:
    im2 = Image.open(file_uploaded)
    st.image(im2, caption='Uploaded Image', use_column_width=True)

count_egg = st.sidebar.button("Count Eggs")

st.cache(persist=True)
if count_egg:
    if file_uploaded is None:

        st.write("Invalid command, please upload an image")
    else:
        with st.spinner('Splitting please wait...'):

            nm_img = file_uploaded.name
            PATH = path + '/' + nm_img
            tiles = image_slicer.slice(PATH, 6)
            image_slicer.save_tiles(tiles, directory=path, \
                                    format='png')
            p = file_uploaded.name.replace('.png', '')
            img1 = Image.open(path + '/' + p + '_01_01.png')
            img2 = Image.open(path + '/' + p + '_01_02.png')
            img3 = Image.open(path + '/' + p + '_01_03.png')
            img4 = Image.open(path + '/' + p + '_02_01.png')
            img5 = Image.open(path + '/' + p + '_02_02.png')
            img6 = Image.open(path + '/' + p + '_02_03.png')
        with st.spinner('Inverting and Resizing please wait...'):

            img1 = img1.resize((1024, 1024))
            img1 = ImageOps.invert(img1)
            img1.save(path + '/' + 'inverted1.png')
            img2 = img2.resize((1024, 1024))
            img2 = ImageOps.invert(img2)
            img2.save(path + '/' + 'inverted2.png')
            img3 = img3.resize((1024, 1024))
            img3 = ImageOps.invert(img3)
            img3.save(path + '/' + 'inverted3.png')
            img4 = img4.resize((1024, 1024))
            img4 = ImageOps.invert(img4)
            img4.save(path + '/' + 'inverted4.png')
            img5 = img5.resize((1024, 1024))
            img5 = ImageOps.invert(img5)
            img5.save(path + '/' + 'inverted5.png')
            img6 = img6.resize((1024, 1024))
            img6 = ImageOps.invert(img6)
            img6.save(path + '/' + 'inverted6.png')

            col1, col2, col3 = st.beta_columns([1, 1, 1])
            col1.image(img1, use_column_width=True)
            col2.image(img2, use_column_width=True)
            col3.image(img3, use_column_width=True)
            col1.image(img4, use_column_width=True)
            col2.image(img5, use_column_width=True)
            col3.image(img6, use_column_width=True)

            img1 = cv2.imread(path + '/' + '_01_01.png')
            img2 = cv2.imread(path + '/' + '_01_02.png')
            img3 = cv2.imread(path + '/' + '_01_03.png')
            img4 = cv2.imread(path + '/' + '_02_01.png')
            img5 = cv2.imread(path + '/' + '_02_02.png')
            img6 = cv2.imread(path + '/' + '_02_03.png')

            st.sidebar.write("--------")
            st.sidebar.write('<span style="color:%s">%s</span>' % ('red', "Image split into 6 parts and resized "
                                                                          "1024*1024 then inverted for using "
                                                                          "detection.  "), unsafe_allow_html=True)
            # with st.spinner('Finding Bounding Boxes please wait...'):

            # img1_o = predict(cfg,img1)
            # img2_o = predict(cfg,img2)
            # img3_o = predict(cfg,img3)
            # img4_o = predict(cfg,img4)
            # img5_o = predict(cfg,img5)
            # img6_o = predict(cfg,img6)

            # im_an1 = viso(img1_o,img1)
            # im_an2 = viso(img2_o,img2)
            # im_an3 = viso(img3_o,img3)
            # im_an4 = viso(img4_o,img4)
            # im_an5 = viso(img5_o,img5)
            # im_an6 = viso(img6_o,img6)

            # col1.write(im_an1, use_column_width=True)
            # col2.write(im_an2, use_column_width=True)
            # col3.write(im_an3, use_column_width=True)
            # col1.write(im_an4, use_column_width=True)
            # col2.write(im_an5, use_column_width=True)
            # col3.write(im_an6, use_column_width=True)

            with st.spinner('Counting eggs please wait...'):
                img1_c = predict(img1)
                img2_c = predict(img2)
                img3_c = predict(img3)
                img4_c = predict(img4)
                img5_c = predict(img5)
                img6_c = predict(img6)

                total = img1_c + img2_c + img3_c + img4_c + img5_c + img6_c

                st.success("We got successfully all total eggs : " + str(total))

