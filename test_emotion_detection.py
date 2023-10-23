from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TesteMotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertNotEqual(result_1['joy'], 0)
        result_2 = emotion_detector('I am really mad about this')
        self.assertNotEqual(result_2['anger'], 0)
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertNotEqual(result_3['disgust'], 0)
        esult_4 = emotion_detector('I am so sad about this')
        self.assertNotEqual(result_1['sadness'], 0)
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertNotEqual(result_2['fear'], 0)

unittest.main()