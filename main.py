import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")
def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n\n쾌적하고 안전한 셔틀버스 이용을 위해 다음과 같이 에티컷을 공지 드리오니\n클러스터 구성원 여러분들의 협조 부탁드리겠습니다.\n\n"
            f"\n"
            f"\n"
            f":k체크: 셔틀버스 내부에서 *음식,음료 취식 하지 않기!*\n"
            f":k체크: 셔틀버스 탑승 간 *전화통화,옆 대화 지양하기!*\n"
            f":k체크: *타 이용객에게 불편을 야기하는 행동 하지 않기!*\n"
            f":k체크: *이어폰을 이용하지 않고 영상시청, 개인사유로 버스 대기 요청 등*\n"
            f":k체크: 셔틀버스 탑승 후 꼭! *안전벨트 착용하기!*\n"
            f"\n"
            f"\n"
            f"*자세한 자료는 스레드 참고 바랍니다!*\n\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
