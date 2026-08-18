[app]
title = TekAI
package.name = tekai
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0.0

requirements = python3,kivy,json,os,random,datetime

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
