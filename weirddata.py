import re

raw_data = '<circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="236" cy="131" r="6" data-qa-id="shot_665db6bddb0af218903abe9e"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="276" cy="29" r="6" data-qa-id="shot_665db6bddb0af218903abfd3"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="340" cy="51" r="6" data-qa-id="shot_665db6bddb0af218903ac082"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="286" cy="86" r="6" data-qa-id="shot_665db6bddb0af218903abe8b"></circle><circle class="Shot--1rzgJsmc Shot--offGoal--29IUNenO" cx="343" cy="99" r="6" data-qa-id="shot_665db6bddb0af218903abf16"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="284" cy="110" r="6" data-qa-id="shot_665db6bddb0af218903ac038"></circle><circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="260" cy="134" r="6" data-qa-id="shot_665db6bddb0af218903ac12e"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="391" cy="102" r="6" data-qa-id="shot_665db6bddb0af218903ac148"></circle><circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="367" cy="83" r="6" data-qa-id="shot_665db6bddb0af218903ac20e"></circle><circle class="Shot--1rzgJsmc Shot--offGoal--29IUNenO" cx="292" cy="279" r="6" data-qa-id="shot_665db6bddb0af218903abe67"></circle><circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="123" cy="247" r="6" data-qa-id="shot_665db6bddb0af218903abf5f"></circle><circle class="Shot--1rzgJsmc Shot--offGoal--29IUNenO" cx="155" cy="222" r="6" data-qa-id="shot_665db6bddb0af218903abfa2"></circle><circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="364" cy="196" r="6" data-qa-id="shot_665db6bddb0af218903ac069"></circle><circle class="Shot--1rzgJsmc Shot--offGoal--29IUNenO" cx="155" cy="244" r="6" data-qa-id="shot_665db6bddb0af218903ac097"></circle><circle class="Shot--1rzgJsmc Shot--offGoal--29IUNenO" cx="439" cy="276" r="6" data-qa-id="shot_665db6bddb0af218903ac0a6"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="359" cy="196" r="6" data-qa-id="shot_665db6bddb0af218903ac0b9"></circle><circle class="Shot--1rzgJsmc Shot--goal--2BEzMz7g" cx="343" cy="190" r="6" data-qa-id="shot_665db6bddb0af218903ac23d"></circle><circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="469" cy="263" r="6" data-qa-id="shot_665db6bddb0af218903ac2af"></circle><circle class="Shot--1rzgJsmc Shot--onGoal--ZUKUY0vC" cx="557" cy="276" r="6" data-qa-id="shot_665db6bddb0af218903ac2f3"></circle>'
data_list = re.findall('(-.{15,19} cx="[0-9]+" cy="[0-9]+)', raw_data)

for i in range(len(data_list)):
    print(re.findall('[abcdefgGklno]{4,7}', data_list[i])[0], re.findall('"[0-9]+', data_list[i])[1][1:],re.findall('"[0-9]+', data_list[i])[0][1:])

