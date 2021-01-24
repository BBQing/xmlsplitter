from xmlsplitter import XmlSplitter            
        
if __name__ == "__main__":
    file_path = 'data/bigfile.xml'
    dest_dir = 'split'
    target_xpath = "/default:something/default:node/default:link"
    XmlSplitter.with_file(target_xpath, 'default', dest_dir , file_path)