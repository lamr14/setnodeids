# setnodeids
Script written in python to set node-IDs in FlockLab

In TelosB nodes, Contiki restores the node ids from the external flash during the boot process. If somebody overwrites that area of the flash, the node id might be different or not set (in case of zero.)
I faced the same problem before. What I did to overcome this problem was to use Contiki shell to reset the node ids to their defaults. I wrote a simple python script for that (see the attachment).
You may have to schedule an addition test before your actual test begins. 

I forgot to mention that you may need to wait until all the nodes are booted into Contiki shell.
Usually, I verify this by looking at the serial output. You can use the "ncat" command for that
For an example, you can monitor the serial output of node 1 as follows
# ncat whymper.ee.ethz.ch 50101

FlockLab supports node ID setting the TinyOS way. That means if you have a global variable called uint16_t TOS_NODE_ID in your program and the program initializes the variable to a specific value, then the test management will automatically assign different node IDs before flashing your nodes. This node ID assignment is basically the only difference in program image treatment in FlockLab, which will be done according to the '<os>'-tag in your test configuration.
If you'd rather prefer to stay with the 'load node ID from flash'-method as used by Contiki, you would have to make sure yourself that the node ID is correctly stored on the flash memory before your test starts. Currently FlockLab does not initialize or alter the flash memory content of the nodes.
