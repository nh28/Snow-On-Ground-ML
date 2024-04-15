from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump, load

class Model:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def create_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        # Instantiate Random Forest classifier with desired parameters
        rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)

        # Train the Random Forest model
        rf_classifier.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = rf_classifier.predict(X_test)

        # Evaluate model performance
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

        dump(rf_classifier, 'SOG_model.joblib')

    @staticmethod
    def predict_data(X):
        model = load('SOG_model.joblib')
        return model.predict(X)