version 1.0

task hello {
    input {
      String name = "World"
    }
    
    command {
        echo "Hello ${name}!"
    }
    output {
        File response = stdout()
    }
}

workflow test_workflow {
  input {
    String name
  }
  
  call hello {
      input:
          name = name
  }
}
