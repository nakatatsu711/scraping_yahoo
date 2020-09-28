import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL = 'https://www.yahoo.co.jp'
URL_TITLE = 'Yahoo! JAPAN'
# 設定値
chromedriver_path = 'ChromeDriverのパス'


def main():
    '''
    メインの処理
    Yahooの検索エンジンで入力したキーワードを検索し、1番目にヒットしたページのURLを取得
    クリックしてページに遷移し、前ページに戻る
    '''

    driver = webdriver.Chrome(chromedriver_path)  # ChromeのWebDriverオブジェクトを作成
    driver.get(URL)  # Yahooのトップページを開く
    time.sleep(2)  # 2秒待機
    assert URL_TITLE in driver.title  # タイトルに'Yahoo! JAPAN'が含まれていることを確認

    key_list = []
    for key in sys.argv:  # ターミナルに入力した検索キーワードのリスト
        if '.py' in key:  # 最初の要素はファイル名なので除外
            continue
        key_list.append(key)
    keyword = ' '.join(key_list)  # 複数のキーワードにも対応

    input_element = driver.find_element_by_name('p')  # 検索テキストボックスの要素をname属性から取得
    input_element.send_keys(keyword)  # 検索テキストボックスにキーワードを入力
    input_element.send_keys(Keys.RETURN)  # Enterキーを送信
    time.sleep(2)  # 2秒待機

    assert keyword in driver.title  # タイトルにkeywordが含まれていることを確認

    url = get_url(driver)
    print('検索キーワード ->', keyword)
    print(url)  # 結果を出力

    driver.quit()  # ブラウザーを閉じる


def get_url(driver):
    '''
    1番目にヒットしたページに遷移し、URLを取得
    '''

    objects = driver.find_elements_by_css_selector('div.Algo > section > div.sw-Card__section > div.sw-Card__headerSpace > div.sw-Card__title > a')  # a要素取得
    object = objects[0]  # 1番目にヒットしたページを指定
    object.click()  # a要素をクリック
    time.sleep(2)  # 2秒待機
    url = driver.current_url  # 遷移ページからURLを取得
    driver.back()  # 前ページに戻る
    time.sleep(2)  # 2秒待機
    return url


if __name__ == '__main__':
    main()
