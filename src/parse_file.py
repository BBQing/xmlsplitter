from xmlsplitter import XmlSplitter            
        


if __name__ == "__main__":
    

    file_path = 'data/bigfile.xml'
    dest_dir = 'split'
    target_xpath = "/default:something/default:node/default:link"
    XmlSplitter.with_file(target_xpath, 'default', dest_dir , file_path)
    # splitter = XmlSplitter(target_xpath)
    # print(splitter.split(file_path, dest_dir))

    # xmlsplitter '/default:something/default:node/default:link' split  data/bigfile.xml
    # xmlsplitter '/ns:something/ns:node/na:link' split  data/bigfile.xml