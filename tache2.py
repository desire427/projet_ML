import matplotlib.pyplot as plt
from tache1 import DataFetcher

class WeatherVisualizer:
    """
    Visualizes weather data using matplotlib
    """
    @staticmethod
    def plot_weather_data(weather_data):
        if not weather_data:
            print("No data to visualize")
            return
            
        plt.figure(figsize=(10, 5))
        
        # Create a simple bar chart
        metrics = ['Temperature', 'Humidity']
        values = [weather_data['temperature'], weather_data['humidity']]
        
        bars = plt.bar(metrics, values, color=['skyblue', 'lightgreen'])
        
        plt.title(f"Weather in {weather_data['city']} ({weather_data['timestamp']})")
        plt.ylabel('Values')
        plt.xlabel('Metrics')
        
        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}',
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    fetcher = DataFetcher("your_api_key_here")  # Same API key as in data_fetcher.py
    data = fetcher.get_weather("Paris")
    
    visualizer = WeatherVisualizer()
    visualizer.plot_weather_data(data)