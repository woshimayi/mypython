vlanCtl_cleanup(void)    ("vlanCtl_cleanup")
vlanCtl_cmdContinue(void)    ("vlanCtl_cmdContinue --continue\n")
vlanCtl_cmdCopyTagCfi(unsigned int sourceTagIndex, unsigned int targetTagIndex)    ("vlanCtl_cmdCopyTagCfi --copy-cfi %d %d\n", sourceTagIndex, targetTagIndex)
vlanCtl_cmdCopyTagEtherType(unsigned int sourceTagIndex, unsigned int targetTagIndex)    ("vlanCtl_cmdCopyTagEtherType --copy-tag-ethertype %d %d\n", sourceTagIndex, targetTagIndex)
vlanCtl_cmdCopyTagPbits(unsigned int sourceTagIndex, unsigned int targetTagIndex)    ("vlanCtl_cmdCopyTagPbits --copy-pbits %d %d\n", sourceTagIndex, targetTagIndex)
vlanCtl_cmdCopyTagVid(unsigned int sourceTagIndex, unsigned int targetTagIndex)    ("vlanCtl_cmdCopyTagVid --copy-vid %d %d\n", sourceTagIndex, targetTagIndex)
vlanCtl_cmdDropFrame(void)    ("vlanCtl_cmdDropFrame --drop-frame\n")
vlanCtl_cmdDscpToPbits(unsigned int tagIndex)    ("vlanCtl_cmdDscpToPbits --dscp2pbits %d\n", tagIndex)
vlanCtl_cmdOvrdLearningVid(unsigned int vid)    ("vlanCtl_cmdOvrdLearningVid --ovrd-learn-vid %d\n", vid)
vlanCtl_cmdPopVlanTag(void)    ("vlanCtl_cmdPopVlanTag --pop-tag\n")
vlanCtl_cmdPushVlanTag(void)    ("vlanCtl_cmdPushVlanTag --push-tag\n")
vlanCtl_cmdSetDscp(unsigned int dscp)    ("vlanCtl_cmdSetDscp --set-dscp %d\n", dscp)
vlanCtl_cmdSetEtherType(unsigned int etherType)    ("vlanCtl_cmdSetEtherType --set-ethertype %#04x\n", etherType)
vlanCtl_cmdSetSkbMarkFlowId(unsigned int flowId)    ("vlanCtl_cmdSetSkbMarkFlowId --set-skb-mark-flowid %d\n", flowId)
vlanCtl_cmdSetSkbMarkPort(unsigned int port)    ("vlanCtl_cmdSetSkbMarkPort --set-skb-mark-port %d\n", port)
vlanCtl_cmdSetSkbMarkQueueByPbits(void)    ("vlanCtl_cmdSetSkbMarkQueueByPbits --set-skb-mark-queue-by-pbits\n")
vlanCtl_cmdSetSkbMarkQueue(unsigned int queue)    ("vlanCtl_cmdSetSkbMarkQueue --set-skb-mark-queue %d\n", queue)
vlanCtl_cmdSetSkbPriority(unsigned int priority)    ("vlanCtl_cmdSetSkbPriority --set-skb-prio %d\n", priority)
vlanCtl_cmdSetTagCfi(unsigned int cfi, unsigned int tagIndex)    ("vlanCtl_cmdSetTagCfi --set-cfi %d %d\n", cfi, tagIndex)
vlanCtl_cmdSetTagEtherType(unsigned int etherType, unsigned int tagIndex)    ("vlanCtl_cmdSetTagEtherType --set-tag-ethertype %#04x %d\n", etherType, tagIndex)
vlanCtl_cmdSetTagPbits(unsigned int pbits, unsigned int tagIndex)    ("vlanCtl_cmdSetTagPbits --set-pbits %d %d\n", pbits, tagIndex)
vlanCtl_cmdSetTagVid(unsigned int vid, unsigned int tagIndex)    ("vlanCtl_cmdSetTagVid --set-vid %d %d\n", vid, tagIndex)
vlanCtl_createVlanFlows(char *rxVlanDevName, char *txVlanDevName)    ("vlanCtl_createVlanFlows"( "--create-flows %s %s\n", rxVlanDevName, txVlanDevName)
vlanCtl_createVlanInterfaceByNameExt(char *realDevName, char *vlanDevName, vlanCtl_createParams_t *createParamsP)    ("vlanCtl_createVlanInterfaceByNameExt --if-create-name %s %s %s %s %s\n",       realDevName, vlanDevName,        createParamsP->isRouted?"--routed":"",       createParamsP->isMulticast?"--mcast":"",       createParamsP->isSwOnly?"--swonly":"")
vlanCtl_createVlanInterfaceByName(char *realDevName, char *vlanDevName, int isRouted, int isMulticast)    ("vlanCtl_createVlanInterfaceByName --if-create-name %s %s %s %s\n",        realDevName, vlanDevName, isRouted?"--routed":"", isMulticast?"--mcast":"")
vlanCtl_createVlanInterfaceExt(const char *realDevName, unsigned int vlanDevId, vlanCtl_createParams_t *createParamsP)    ("vlanCtl_createVlanInterfaceExt --if-create %s %d %s %s %s\n",       realDevName, vlanDevId,       createParamsP->isRouted?"--routed":"",       createParamsP->isMulticast?"--mcast":"",       createParamsP->isSwOnly?"--swonly":"")
vlanCtl_createVlanInterface(const char *realDevName, unsigned int vlanDevId, int isRouted, int isMulticast)    ("vlanCtl_createVlanInterface --if-create %s %d %s %s\n",        realDevName, vlanDevId, isRouted?"--routed":"", isMulticast?"--mcast":"")
vlanCtl_deleteVlanFlows(char *rxVlanDevName, char *txVlanDevName)    ("vlanCtl_deleteVlanFlows"( "--delete-flows %s %s\n", rxVlanDevName, txVlanDevName)
vlanCtl_deleteVlanInterface(char *vlanDevName)    ("vlanCtl_deleteVlanInterface --if-delete %s\n", vlanDevName)
vlanCtl_dumpAllRules(void)    ("vlanCtl_dumpAllRules --rule-dump-all\n")
vlanCtl_dumpDscpToPbits(char *realDevName, unsigned int dscp)    ("vlanCtl_dumpDscpToPbits");    if (dscp == VLANCTL_DONT_CARE)        ( "--if %s --show-dscp2pbits\n", realDevName);    else        ( "--if %s --dscp %d --<cmd_not support>\n", realDevName, dscp)
vlanCtl_dumpLocalStats(char *realDevName)    ("vlanCtl_dumpLocalStats --local-stats %s\n", realDevName)
vlanCtl_dumpRuleTable(char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags)    ("vlanCtl_dumpRuleTable --if %s --%s --tags %d --show-table\n",        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx",       nbrOfTags)
vlanCtl_dumpTpidTable(char *realDevName)    ("vlanCtl_dumpTpidTable --if %s --show-tpid\n", realDevName)
vlanCtl_filterOnDscp2Pbits(unsigned int dscp2pbits)    ("vlanCtl_filterOnDscp2Pbits --filter-dscp2pbits %d\n", dscp2pbits)
vlanCtl_filterOnDscp(unsigned int dscp)    ("vlanCtl_filterOnDscp --filter-dscp %d\n", dscp)
vlanCtl_filterOnEthertype(unsigned int etherType)    ("vlanCtl_filterOnEthertype --filter-ethertype %#04x\n", etherType)
vlanCtl_filterOnFlags(unsigned int flags)    ("vlanCtl_filterOnFlags"if(flags&BCM_VLAN_FILTER_FLAGS_IS_UNICAST)	    ("--filter-unicast\n"if(flags&BCM_VLAN_FILTER_FLAGS_IS_MULTICAST)	    ("--filter-multicast\n"if(flags&BCM_VLAN_FILTER_FLAGS_IS_BROADCAST)	    ("--filter-broadcast\n")
vlanCtl_filterOnIpProto(unsigned int ipProto)    ("vlanCtl_filterOnIpProto --filter-ipproto %d\n", ipProto)
vlanCtl_filterOnRxRealDevice(char *realDevName)    ("vlanCtl_filterOnRxRealDevice --filter-rxif %s\n", realDevName)
vlanCtl_filterOnSkbMarkFlowId(unsigned int flowId)    ("vlanCtl_filterOnSkbMarkFlowId --filter-skb-mark-flowid %d\n", flowId)
vlanCtl_filterOnSkbMarkPort(unsigned int port)    ("vlanCtl_filterOnSkbMarkPort --filter-skb-mark-port %d\n", port)
vlanCtl_filterOnSkbPriority(unsigned int priority)    ("vlanCtl_filterOnSkbPriority --filter-skb-prio %d\n", priority)
vlanCtl_filterOnTagCfi(unsigned int cfi, unsigned int tagIndex)    ("vlanCtl_filterOnTagCfi --filter-cfi %d %d\n", cfi, tagIndex)
vlanCtl_filterOnTagEtherType(unsigned int etherType, unsigned int tagIndex)    ("vlanCtl_filterOnTagEtherType --filter-tag-ethertype %#04x %d\n", etherType, tagIndex)
vlanCtl_filterOnTagPbits(unsigned int pbits, unsigned int tagIndex)    ("vlanCtl_filterOnTagPbits --filter-pbits %d %d\n", pbits, tagIndex)
vlanCtl_filterOnTagVid(unsigned int vid, unsigned int tagIndex)    ("vlanCtl_filterOnTagVid --filter-vid %d %d\n", vid, tagIndex)
vlanCtl_filterOnTxVlanDevice(char *vlanDevName)    ("vlanCtl_filterOnTxVlanDevice --filter-txif %s\n", vlanDevName)
vlanCtl_filterOnVlanDeviceMacAddr(unsigned int acceptMulticast)    ("vlanCtl_filterOnVlanDeviceMacAddr --filter-vlan-dev-mac-addr %d\n", acceptMulticast)
vlanCtl_getNbrOfRulesInTable(char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags)    ("vlanCtl_getNbrOfRulesInTable --if %s --%s --tags %d --<cmd_not_support>\n",        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx",       nbrOfTags)
vlanCtl_initTagRule(void)    ("vlanCtl_initTagRule")
vlanCtl_init(void)    ("vlanCtl_init")
vlanCtl_insertTagRule(const char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags, vlanCtl_ruleInsertPosition_t position, unsigned int posTagRuleId)    ("vlanCtl_insertTagRule --if %s --%s --tags %d\n",        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx",       nbrOfTags);    if (position == VLANCTL_POSITION_APPEND)        (--->, "--rule-append\n");    else if (position == VLANCTL_POSITION_LAST)        (--->, "--rule-insert-last\n");    else if (position == VLANCTL_POSITION_BEFORE)        (--->, "--rule-insert-before %d\n", posTagRuleId);    else if (position == VLANCTL_POSITION_AFTER)        (--->, "--rule-insert-after %d\n", posTagRuleId)
vlanCtl_removeAllTagRule(char *vlanDevName)    ("vlanCtl_removeAllTagRule --rule-remove-all %s\n", vlanDevName)
vlanCtl_removeTagRuleByFilter(char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags)    ("vlanCtl_removeTagRuleByFilter --if %s --%s --tags %d\n",        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx",       nbrOfTags);    (--->, "--rule-remove-by-filter\n")
vlanCtl_removeTagRule(char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags, unsigned int tagRuleId)    ("vlanCtl_removeTagRule --if %s --%s --tags %d --rule-remove %d\n",        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx",       nbrOfTags, tagRuleId)
vlanCtl_setDefaultAction(const char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags, vlanCtl_defaultAction_t defaultAction, char *defaultRxVlanDevName)    ("vlanCtl_setDefaultAction"if( (tableDir == VLANCTL_DIRECTION_RX) && (defaultAction == VLANCTL_ACTION_ACCEPT))	    ( "--if %s --rx --tags %d --default-miss-accept %s\n", realDevName, nbrOfTags, defaultRxVlanDevName);    else	    ( "--if %s --%s --tags %d --%s\n", 	        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx", nbrOfTags, 	        defaultAction == VLANCTL_ACTION_ACCEPT ? "default-miss-accept":"default-miss-drop")
vlanCtl_setDefaultVlanTag(char *realDevName, vlanCtl_direction_t tableDir, unsigned int nbrOfTags, unsigned int defaultTpid, unsigned int defaultPbits, unsigned int defaultCfi,                              unsigned int defaultVid)    ("vlanCtl_setDefaultVlanTag --if %s --%s --tags %d",        realDevName, tableDir == VLANCTL_DIRECTION_RX ? "rx":"tx",       nbrOfTagsif(cmsActionTraceEnable_g)	{	    if (defaultTpid != VLANCTL_DONT_CARE)	        __print(" --default-tpid %d", defaultTpid    if (defaultPbits != VLANCTL_DONT_CARE)	        __print(" --default-pbits %d", defaultPbits    if (defaultCfi != VLANCTL_DONT_CARE)	        __print(" --default-cfi %d", defaultCfi    if (defaultVid != VLANCTL_DONT_CARE)	        __print(" --default-vid %d", defaultVid    __print("\n"}    ;
vlanCtl_setDropPrecedence(bcmVlan_flowDir_t dir, bcmVlan_dpCode_t dpCode)    ("vlanCtl_setDropPrecedence --dir %d, --dpcode %d\n", dir, dpCode)
vlanCtl_setDscpToPbits(char *realDevName, unsigned int dscp, unsigned int pbits)    ("vlanCtl_setDscpToPbits --if %s --cfg-dscp2pbits %d %d\n",        realDevName, dscp, pbits)
vlanCtl_setIfSuffix(char *ifSuffix)    ("vlanCtl_setIfSuffix --if-suffix %s\n", ifSuffix)
vlanCtl_setIptvOnly(void)    ("vlanCtl_setIptvOnly --set-iptv\n")
vlanCtl_setRealDevMode(char *realDevName, bcmVlan_realDevMode_t mode)    ("vlanCtl_setRealDevMode"( "--if %s --%s\n", realDevName, mode == BCM_VLAN_MODE_ONT ? "set-if-mode-ont":"set-if-mode-rg")
vlanCtl_setReceiveVlanDevice(char *vlanDevName)    ("vlanCtl_setReceiveVlanDevice --set-rxif %s\n", vlanDevName)
vlanCtl_setTpidTable(char *realDevName, unsigned int *tpidTable)    ("vlanCtl_setTpidTable --if %s --cfg-tpid", realDevNameif(cmsActionTraceEnable_g)	{	    for(i=0; i<BCM_VLAN_MAX_TPID_VALUES; ++i)	    {	        __print(" %d", tpidTable[i]    }	    __print("\n"}
vlanCtl_setVlanRuleTableType(unsigned int type)    ("vlanCtl_setVlanRuleTableType --rule-type %d\n", type)