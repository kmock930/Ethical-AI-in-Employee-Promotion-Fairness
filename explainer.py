import numpy as np
from lime.lime_text import LimeTextExplainer
from lime.lime_tabular import LimeTabularExplainer

class LIMEExplainer:
    def __init__(self, model, feature_names):
        self.model = model
        self.feature_names = feature_names

    # Custom Predict Proba with tensorflow's probability
    # https://www.tensorflow.org/probability
    def predict_proba(self, inputs):
        if not isinstance(inputs, np.ndarray):
            inputs = np.array(inputs)
        if hasattr(inputs, "toarray"):  # Check if the input has a .toarray() method
            inputs = inputs.toarray()
        # Make Prediction
        return self.model.predict(inputs)

    def explain(self, features, testData, trainingData):
        if (isinstance(testData, str)):
            explainer = LimeTextExplainer(class_names=features)
        else:
            explainer = LimeTabularExplainer(
                training_data=trainingData,
                feature_names=self.feature_names,
                class_names=features,
                mode="classification",
            )
        if (hasattr(self.model, "predict_proba")):
            self.predict_proba = self.model.predict_proba
        exp = explainer.explain_instance(
           testData, self.predict_proba, num_features=len(features)
        )
        exp.as_list()
        # PyPlot
        fig = exp.as_pyplot_figure()
        return exp, fig

