## Possible issue with Conan 2
- Tried with both conan 2.3.1 and conan 2.14.0

I noticed I was getting strange behaviour with a chain of libaries I'm working on. Things woould build fine and then seemingly randomly things would fail to even configure again.
I managed to boil it down to this minimal example where I have one base library that includes some vulkan dependencies. I then have a minimal application that includes the library
as a dependency.  
When I install and configure the application (b) things work as expected at first. Then if I run `conan install` again, the configure step falls over trying to find the vulkan-headers
path. It seems the path conan refers to changes over the two installs. The error is as follows.
```
CMake Error in CMakeLists.txt:                                                                 
  Imported target "useless_a::useless_a" includes non-existent path                            
                                                                                               
    "/home/mcotton/.conan2/p/b/vulka1ff196a74a5d8/p/include"                  
                                                                                               
  in its INTERFACE_INCLUDE_DIRECTORIES.  Possible reasons include:                             
                                                                                               
  * The path was deleted, renamed, or moved to another location.                               
                                                                                               
  * An install or uninstall procedure did not complete successfully.         
                                               
  * The installation package was faulty and references files it does not                       
  provide.
```
I'm unsure if it's something I'm doing incorrectly or if it's an issue with the vulkan packages, or if it's even an issue with conan itself.

I have created a small bash script which demonstrates the issue I'm seeing. Hopefully this is reproducable and fixable.
