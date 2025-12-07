# LLM教學

## 前置作業

1. 需現在本地端架設Ollama。
2. 需要有OpenAI API。

## 環境建置

採用uv專案管理，uv安裝方式請參考[官方說明](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)。

下載此專案，執行以下指令:
```
uv sync
```

建立`.env`檔案，裡面輸入以下內容:
```
OPENAI_API_KEY=[你的OpenAI API Key]
```

## 教學講義
* [生成式AI應用於財務投資-1(HackMD講義)](https://hackmd.io/@suyenting/r1SEpdUGll)
    * 程式環境建立：Python、OpenAI、Ollama與Open WebUI
* [ChatGPT使用方法與範例分享(HackMD講義)](https://hackmd.io/@suyenting/SyHUGS9Qxe)
    * 圖像辨識與分析
    * 圖像生成
    * 文件處理功能
    * 搜尋網頁功能
    * 深入研究(Deep Research)
    * 編寫或編碼(Canva)
    * GPT Store應用
* [生成式AI應用於財務投資-2(HackMD講義)](https://hackmd.io/@suyenting/rktFuEbXee)
    * LLM的AI幻覺
    * 如何避免LLM的AI幻覺
    * LangChain介紹
    * LangChain實作
* [生成式AI應用於財務投資-3(HackMD講義)](https://hackmd.io/@suyenting/Skpesz2Vee)
    * Function Calling介紹
    * Agent介紹
    * 生成式AI應用財務投資之GitHub專案介紹
* [生成式AI應用於財務投資-4(HackMD講義)](https://hackmd.io/@suyenting/SJAV875Uxe)
    * Git介紹
    * GitHub: TauricResearch/TradingAgents專案部署實作
* [生成式AI應用於財務投資-5(Google Slide)](https://docs.google.com/presentation/d/10JUK1qgpxhPS6GOOLNHgT581y_qZmVMHZKkMgYgN5lY/edit?usp=sharing)
    * 學術文章介紹: [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)
* [生成式AI應用於財務投資-6(HackMD講義)](https://hackmd.io/@suyenting/HyE3SUqLeg)
    * MCP介紹
    * Gemini CLI
    * Gemini CLI加入MCP Server
    * 用Python撰寫自己的MCP Server
* [生成式AI應用於財務投資-7(HackMD講義)](https://hackmd.io/@suyenting/SJkqN6Coel)
    * LangGraph介紹與程式教學
    * LangCahin與LangGraph的差異
    * LangGraph程式教學
* [生成式AI應用於財務投資-8(HackMD講義)](https://hackmd.io/@suyenting/BJsnw7YTxe)
    * PostgreSQL介紹與程式教學
* [生成式AI應用於財務投資-9(HackMD講義)](https://hackmd.io/@suyenting/ByuDS86kZl)
    * SQL Agent(LangCahin + SQLDatabaseToolkit)使用方式介紹
    * HTML語法介紹
    * 網路爬蟲介紹
* [生成式AI應用於財務投資-10(HackMD講義)](https://hackmd.io/@suyenting/SyK1YRn0xl)
    * Selenium爬蟲
    * 自動化排程