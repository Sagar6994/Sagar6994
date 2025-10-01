[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of modules to blacklist
source.exclude_strs = tests,docs,bin,buildozer.spec

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
requirements.source.kivy = ../../kivy

# (str) Presplash background color (for new android presplash)
#android.presplash_color = #FFFFFF

# (str) Presplash animation using Lottie format.
#android.presplash_lottie = "path/to/your/lottie/file.json"

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash image
#presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
#android.api = 27

# (int) Minimum API required
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (str) Android NDK path. If not set, will be downloaded automatically
#android.ndk_path =

# (str) Android SDK path. If not set, will be downloaded automatically
#android.sdk_path =

# (str) ANT path. If not set, will be downloaded automatically
#android.ant_path =

# (bool) If True, then skip the build if recipes are source folder recipes.
# This is useful if you just want to create the project folder and not build
# the requirements.
#android.skip_build = False

#
# iOS specific
#

# (str) The Xcode project to use
#ios.project_name = 'kivyapp'

#
# Python for android (p4a) specific
#

# (str) p4a url to download for building the distribution
#p4a.url =

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#p4a.arch = armeabi-v7a

# (str) The p4a branch to use for building the distribution
#p4a.branch = master

# (str) The p4a git repository to use for building the distribution
#p4a.source_dir =

#
# Buildozer specific
#

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to buildozer.spec file
#spec.filename = buildozer.spec

# (str) buildozer path, if not set, will be created automatically
#buildozer.build_dir = ./.buildozer

# (str) Path to buildozer bin folder
#buildozer.bin_dir = ./.buildozer/bin

# (str) Path to buildozer android platform folder
#buildozer.platform_dir = ./.buildozer/android/platform

# (str) p4a path, if not set, will be created automatically
#p4a.source_dir = ./.buildozer/android/platform/python-for-android

# (str) The name of the executable file to create
#bin_name = myapp

# (str) The name of the zip file to create
#zip_name = myapp.zip

# (str) The name of the tar.gz file to create
#tar_name = myapp.tar.gz

# (str) The name of the tar.bz2 file to create
#tar_name = myapp.tar.bz2

# (str) The name of the dmg file to create (mac only)
#dmg_name = myapp.dmg

# (str) The name of the app file to create (mac only)
#app_name = myapp

# (str) The name of the ipa file to create (ios only)
#ipa_name = myapp.ipa

# (str) The name of the apk file to create
#apk_name = myapp

# (str) The name of the aab file to create
#aab_name = myapp

# (str) The name of the exe file to create (windows only)
#exe_name = myapp

# (str) The name of the msi file to create (windows only)
#msi_name = myapp

# (str) The name of the deb file to create (linux only)
#deb_name = myapp

# (str) The name of the rpm file to create (linux only)
#rpm_name = myapp

# (str) The name of the snap file to create (linux only)
#snap_name = myapp

# (str) The name of the flatpak file to create (linux only)
#flatpak_name = myapp

# (str) The name of the appimage file to create (linux only)
#appimage_name = myapp

# (str) The name of the pgo file to create (linux only)
#pgo_name = myapp

# (str) The name of the whl file to create
#whl_name = myapp

# (str) The name of the json file to create
#json_name = myapp

# (str) The name of the xml file to create
#xml_name = myapp

# (str) The name of the yml file to create
#yml_name = myapp

# (str) The name of the toml file to create
#toml_name = myapp

# (str) The name of the ini file to create
#ini_name = myapp

# (str) The name of the cfg file to create
#cfg_name = myapp

# (str) The name of the conf file to create
#conf_name = myapp

# (str) The name of the sh file to create
#sh_name = myapp

# (str) The name of the bat file to create (windows only)
#bat_name = myapp

# (str) The name of the ps1 file to create (windows only)
#ps1_name = myapp

# (str) The name of the vbs file to create (windows only)
#vbs_name = myapp

# (str) The name of the scpt file to create (mac only)
#scpt_name = myapp

# (str) The name of the applescript file to create (mac only)
#applescript_name = myapp

# (str) The name of the js file to create
#js_name = myapp

# (str) The name of the ts file to create
#ts_name = myapp

# (str) The name of the css file to create
#css_name = myapp

# (str) The name of the html file to create
#html_name = myapp

# (str) The name of the md file to create
#md_name = myapp

# (str) The name of the rst file to create
#rst_name = myapp

# (str) The name of the txt file to create
#txt_name = myapp

# (str) The name of the log file to create
#log_name = myapp

# (str) The name of the dat file to create
#dat_name = myapp

# (str) The name of the db file to create
#db_name = myapp

# (str) The name of the sql file to create
#sql_name = myapp

# (str) The name of the csv file to create
#csv_name = myapp

# (str) The name of the tsv file to create
#tsv_name = myapp

# (str) The name of the xls file to create (windows only)
#xls_name = myapp

# (str) The name of the xlsx file to create (windows only)
#xlsx_name = myapp

# (str) The name of the doc file to create (windows only)
#doc_name = myapp

# (str) The name of the docx file to create (windows only)
#docx_name = myapp

# (str) The name of the ppt file to create (windows only)
#ppt_name = myapp

# (str) The name of the pptx file to create (windows only)
#pptx_name = myapp

# (str) The name of the pdf file to create
#pdf_name = myapp

# (str) The name of the png file to create
#png_name = myapp

# (str) The name of the jpg file to create
#jpg_name = myapp

# (str) The name of the jpeg file to create
#jpeg_name = myapp

# (str) The name of the gif file to create
#gif_name = myapp

# (str) The name of the bmp file to create
#bmp_name = myapp

# (str) The name of the ico file to create (windows only)
#ico_name = myapp

# (str) The name of the icns file to create (mac only)
#icns_name = myapp

# (str) The name of the svg file to create
#svg_name = myapp

# (str) The name of the tiff file to create
#tiff_name = myapp

# (str) The name of the webp file to create
#webp_name = myapp

# (str) The name of the mp3 file to create
#mp3_name = myapp

# (str) The name of the ogg file to create
#ogg_name = myapp

# (str) The name of the wav file to create
#wav_name = myapp

# (str) The name of the mp4 file to create
#mp4_name = myapp

# (str) The name of the webm file to create
#webm_name = myapp

# (str) The name of the mkv file to create
#mkv_name = myapp

# (str) The name of the avi file to create
#avi_name = myapp

# (str) The name of the mov file to create
#mov_name = myapp

# (str) The name of the wmv file to create (windows only)
#wmv_name = myapp

# (str) The name of the flv file to create
#flv_name = myapp

# (str) The name of the swf file to create
#swf_name = myapp

# (str) The name of the zip file to create
#zip_name = myapp

# (str) The name of the tar file to create
#tar_name = myapp

# (str) The name of the tgz file to create
#tgz_name = myapp

# (str) The name of the tar.gz file to create
#tar_gz_name = myapp

# (str) The name of the tar.bz2 file to create
#tar_bz2_name = myapp

# (str) The name of the tar.xz file to create
#tar_xz_name = myapp

# (str) The name of the 7z file to create (windows only)
#seven_zip_name = myapp

# (str) The name of the rar file to create (windows only)
#rar_name = myapp

# (str) The name of the gz file to create
#gz_name = myapp

# (str) The name of the bz2 file to create
#bz2_name = myapp

# (str) The name of the xz file to create
#xz_name = myapp

# (str) The name of the lzma file to create
#lzma_name = myapp

# (str) The name of the lz4 file to create
#lz4_name = myapp

# (str) The name of the zst file to create
#zst_name = myapp

# (str) The name of the brotli file to create
#brotli_name = myapp

# (str) The name of the snappy file to create
#snappy_name = myapp

# (str) The name of the lzo file to create
#lzo_name = myapp

# (str) The name of the lzham file to create
#lzham_name = myapp

# (str) The name of the lzfse file to create (mac only)
#lzfse_name = myapp

# (str) The name of the lzvn file to create (mac only)
#lzvn_name = myapp

# (str) The name of the lzma2 file to create
#lzma2_name = myapp

# (str) The name of the lzma8 file to create
#lzma8_name = myapp

# (str) The name of the lzma9 file to create
#lzma9_name = myapp

# (str) The name of the lzmat file to create
#lzmat_name = myapp

# (str) The name of the lzma_sdk file to create
#lzma_sdk_name = myapp

# (str) The name of the lzma_sdk_mt file to create
#lzma_sdk_mt_name = myapp

# (str) The name of the lzma_sdk_s file to create
#lzma_sdk_s_name = myapp

# (str) The name of the lzma_sdk_st file to create
#lzma_sdk_st_name = myapp

# (str) The name of the lzma_sdk_mt_s file to create
#lzma_sdk_mt_s_name = myapp

# (str) The name of the lzma_sdk_mt_st file to create
#lzma_sdk_mt_st_name = myapp

# (str) The name of the lzma_sdk_mt_s_st file to create
#lzma_sdk_mt_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s file to create
#lzma_sdk_mt_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st file to create
#lzma_sdk_mt_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = myapp

# (str) The name of the lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s file to create
#lzma_sdk_mt_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_st_s_name = mya