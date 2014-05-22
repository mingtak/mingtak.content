PLONE 的模組開發框架： zopeskel
====================================

zopeskel是plone預設使用的開發框架工具，可以完整的將所需要的工能，預先執行，包括：

 * 登錄zcml,

 * 預先載入(import)相關模組,

 * 預先定義相關class,

 * profile預先設定,

等等各項，讓開發者可以直接進入開發程序，不用進行繁瑣的例行設定

zopeskel在plone 4.3之後被正式收錄，但預設未啟動，必需執行： ::

  bin/plonectl -Nc develop.cfg

執行後在bin目錄底下，會新增zopeskel及其相關指令，我們會在之後一一介紹使用方法。

目錄
------------------------------


.. toctree::
   :maxdepth: 2
   :titlesonly:

   zopeskel_initial
   zopeskel_paster

