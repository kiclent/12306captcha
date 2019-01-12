#coding=utf-8
'''
12306 captcha recognize
kiclent@yahoo.com
test by: Python 3.6, Tensorflow 1.7.1
'''
import numpy as np
import tensorflow as tf
import cv2

class CaptchaModel(object):
    def __init__(self, ocr_model_meta, ocr_model_para, cap_model_meta, cap_model_para):
        self.sess_ocr, self.tensors_ocr = self.restore_sess(ocr_model_meta, ocr_model_para)
        self.sess_cap, self.tensors_cap = self.restore_sess(cap_model_meta, cap_model_para)


    def predict(self, img_path):
        imgs, img_word = self.get_test_image(img_path)

        word_ind = self.ocr_predict(img_word).reshape(-1)
        objs_ind = self.obj_predict(imgs).reshape(-1)

        return word_ind, objs_ind

    def ocr_predict(self, img_word):
        ocr_feed_dict = {
            self.tensors_ocr["tf_X"]: np.array([img_word]),
            self.tensors_ocr["training_flag"]: False,
            self.tensors_ocr["dropout_rate"]: 0.2
        }

        word_c = self.sess_ocr.run(self.tensors_ocr["predictions"], feed_dict=ocr_feed_dict)
        return word_c


    def obj_predict(self, imgs):
        cap_feed_dict = {
            self.tensors_cap["tf_X"]: imgs,
            self.tensors_cap["training_flag"]: False,
            self.tensors_cap["dropout_rate"]: 0.2
        }
        objs_c = self.sess_cap.run(self.tensors_cap["predictions"], feed_dict=cap_feed_dict)
        return objs_c

    # 把验证码的关键字、各个识别的图像剪切出来, 如果需要识别的验证码大小改变则需要作相应的调整
    def captcha_to_patch(self, img):
        imgs = []
        h, w = 66, 66
        indices = [[40, 5], [40, 77], [40, 149], [40, 221],
                   [112, 5], [112, 77], [112, 149], [112, 221]]
        for ind in indices:
            imgs.append(img[ind[0]:ind[0] + h, ind[1]:ind[1] + w])

        imgs = np.array(imgs)

        h, w = 28, 60
        h0, w0 = 0, 118
        img_word = img[h0:h0 + h, w0:w0 + w]

        return imgs, img_word

    def get_test_image(self, image_path):
        im = cv2.imread(image_path)
        im = np.array(im, np.float32)
        if len(im.shape) < 3:
            im = np.stack((im, im, im), axis=2)
        im = im[:, :, [2, 1, 0]]
        im = im * 2.0 / 255 - 1

        imgs, img_word = self.captcha_to_patch(im)

        return imgs, img_word


    def restore_sess(self, model_meta_path, model_para_path):
        graph = tf.Graph()
        print('building new graph:', graph)
        with graph.as_default():
            saver = tf.train.import_meta_graph(model_meta_path)

        gpu_options = tf.GPUOptions(allow_growth=True)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options), graph=graph)
        saver.restore(sess, model_para_path)
        tensors = {}
        tensors["tf_X"] = graph.get_tensor_by_name("tf_X:0")
        tensors["training_flag"] = graph.get_tensor_by_name("training_flag:0")
        tensors["dropout_rate"] = graph.get_tensor_by_name("dropout_rate:0")
        tensors["predictions"] = graph.get_tensor_by_name("predictions:0")
        return sess, tensors

    def close(self):
        self.sess_cap.close()
        self.sess_cap.close()





