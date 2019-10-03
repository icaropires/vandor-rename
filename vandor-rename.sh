vandor-rename(){
  if [ $# -ne 3 ]; then
    echo "Usage example: rename_vandor [class_name] [your_name] [your_registration_number]"
  else
      for f in $(ls aula*.sql aula*.brM3 aula*.pdf aula*.doc 2>/dev/null); do
        class=$1
        typee=$(echo $f | cut -d '_' -f 2)
        name="$2"
        registration_number="$3"
        ext=${f##*.}
      
        mv "$f" "${class}_${typee}_${name}_${registration_number}.${ext}" 2>/dev/null
      done
  fi
}
