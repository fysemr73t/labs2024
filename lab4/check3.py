import aspose.words as aw
import sys

if __name__=="__main__":
    info = aw.FileFormatUtil.detect_file_format(sys.argv[1])
    print(f"encoding: {info.encoding}")
    print(f"type: {info.get_type()} ")
    print(f"has_digital_signature: {info.has_digital_signature}")
    print(f"has_macros: {info.has_macros} ")
    print(f"is_encrypted: {info.is_encrypted}")

    doc = aw.Document(sys.argv[1], aw.loading.LoadOptions(sys.argv[2]))
    print("pages:",doc.page_count)
