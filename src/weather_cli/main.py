import sys
import requests

def get_weather(city: str):
    # 使用 wttr.in 这个极客专属的免费天气 API
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        response.raise_for_status() # 检查请求是否成功
        print(f"当前天气: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"获取天气失败: {e}")

if __name__ == "__main__":
    # 检查用户有没有输入城市名
    if len(sys.argv) > 1:
        city = sys.argv[1]
        get_weather(city)
    else:
        print("用法: uv run src/weather_cli/main.py <城市名>")
