import requests
import re
from requests_html import HTMLSession

def Get_booking_dest_id(Keyword):
    session = HTMLSession()
    url = 'https://www.booking.com/searchresults.en-gb.html?ss={}'.format(Keyword)

    r = session.get(url)
    get_html = r.html.html
    dest_id=re.findall('dest_id=(.*?)&',get_html)[0]
    return dest_id

def Get_booking_hotel(Keyword, checkin,checkout):
    dest_id=Get_booking_dest_id(Keyword)
    headers = {
    'authority': 'www.booking.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.booking.com',
    # 'referer': 'https://www.booking.com/searchresults.en-gb.html?label=zh-cn-ca-booking-desktop-MSet8TH2wsVFXnIfy6N38gS654267613646%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9000414%3Ali%3Adec%3Adm&aid=2311236&ss=%E9%AD%81%E5%8C%97%E5%85%8B%E5%B8%82%2C+%E5%8A%A0%E6%8B%BF%E5%A4%A7&efdco=1&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-571851&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&soz=1&lang_changed=1&offset=25',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-booking-context-action-name': 'searchresults_irene',
    'x-booking-context-aid': '2311236',
    'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTY5NjE2MDU3NywiZXhwIjoxNjk2MjQ2OTc3fQ.1nENvD6If_yciWzFu_55XoZsy-fq22byZXe0xxXKSVvGHyEQ8JcF6TpsI5HKVhLHVflPHs9x6aoj0ebKsZI5qA',
    'x-booking-et-serialized-state': 'Ep2ysrffnOVc9QRbePWFZkYBVWqzCcVXb3LwoZpf-PtE7Mm2RJGmPMbqQxPFGNLeD',
    'x-booking-pageview-id': '67915260264f0254',
    'x-booking-site-type-id': '1',
    'x-booking-topic': 'capla_browser_b-search-web-searchresults',
    }

    params = {
        'ss': Keyword,
        'ssne': Keyword,
        'ssne_untouched': Keyword,
        'label': 'zh-cn-ca-booking-desktop-MSet8TH2wsVFXnIfy6N38gS654267613646%25253Apl%25253Ata%25253Ap1%25253Ap2%25253Aac%25253Aap%25253Aneg%25253Afi%25253Atikwd-65526620%25253Alp9000414%25253Ali%25253Adec%25253Adm',
        'aid': '2311236',
        'lang': 'en-gb',
        'sb': '1',
        'src_elem': 'sb',
        'src': 'searchresults',
        'dest_id': dest_id,
        'dest_type': 'city',
        'checkin': checkin,
        'checkout': checkout,
        'group_adults': '2',
        'no_rooms': '1',
        'group_children': '0',
    }

    json_data = {
        'operationName': 'FullSearch',
        'variables': {
            'input': {
                'acidCarouselContext': None,
                'childrenAges': [],
                'dates': {
                    'checkin': checkin,
                    'checkout': checkout,
                },
                'doAvailabilityCheck': False,
                'encodedAutocompleteMeta': None,
                'enableCampaigns': True,
                'filters': {},
                'forcedBlocks': None,
                'location': {
                    'searchString': Keyword,
                    'destType': 'CITY',
                    'destId': int(dest_id),
                },
                'metaContext': {
                    'metaCampaignId': 0,
                    'externalTotalPrice': None,
                    'feedPrice': None,
                    'hotelCenterAccountId': None,
                    'rateRuleId': None,
                    'dragongateTraceId': None,
                },
                'nbRooms': 1,
                'nbAdults': 2,
                'nbChildren': 0,
                'showAparthotelAsHotel': True,
                'needsRoomsMatch': False,
                'optionalFeatures': {
                    'forceArpExperiments': True,
                    'testProperties': False,
                },
                'pagination': {
                    'rowsPerPage': 25,
                    'offset': 0,
                },
                'referrerBlock': None,
                'sbCalendarOpen': False,
                'sorters': {
                    'selectedSorter': None,
                    'referenceGeoId': None,
                    'tripTypeIntentId': None,
                },
                'travelPurpose': 2,
                'seoThemeIds': [],
                'useSearchParamsFromSession': True,
            },
            'geniusVipUI': {
                'enableEnroll': True,
                'page': 'SEARCH_RESULTS',
            },
        },
        'extensions': {},
        'query': 'query FullSearch($input: SearchQueryInput!, $geniusVipUI: GeniusVipUIsInput) {\n  searchQueries {\n    search(input: $input) {\n      ...FullSearchFragment\n      __typename\n    }\n    __typename\n  }\n  geniusVipEnrolledProgram(input: $geniusVipUI) {\n    ...geniusVipEnrolledProgram\n    __typename\n  }\n}\n\nfragment FullSearchFragment on SearchQueryOutput {\n  banners {\n    ...Banner\n    __typename\n  }\n  breadcrumbs {\n    ... on SearchResultsBreadcrumb {\n      ...SearchResultsBreadcrumb\n      __typename\n    }\n    ... on LandingPageBreadcrumb {\n      ...LandingPageBreadcrumb\n      __typename\n    }\n    __typename\n  }\n  carousels {\n    ...Carousel\n    __typename\n  }\n  destinationLocation {\n    ...DestinationLocation\n    __typename\n  }\n  entireHomesSearchEnabled\n  dateFlexibilityOptions {\n    enabled\n    __typename\n  }\n  filters {\n    ...FilterData\n    __typename\n  }\n  appliedFilterOptions {\n    ...FilterOption\n    __typename\n  }\n  recommendedFilterOptions {\n    ...FilterOption\n    __typename\n  }\n  pagination {\n    nbResultsPerPage\n    nbResultsTotal\n    __typename\n  }\n  tripTypes {\n    ...TripTypesData\n    __typename\n  }\n  results {\n    ...BasicPropertyData\n    ...MatchingUnitConfigurations\n    ...PropertyBlocks\n    ...BookerExperienceData\n    priceDisplayInfoIrene {\n      ...PriceDisplayInfoIrene\n      __typename\n    }\n    licenseDetails {\n      nextToHotelName\n      __typename\n    }\n    inferredLocationScore\n    trackOnView {\n      experimentTag\n      __typename\n    }\n    topPhotos {\n      highResUrl {\n        relativeUrl\n        __typename\n      }\n      lowResUrl {\n        relativeUrl\n        __typename\n      }\n      highResJpegUrl {\n        relativeUrl\n        __typename\n      }\n      lowResJpegUrl {\n        relativeUrl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  searchMeta {\n    ...SearchMetadata\n    __typename\n  }\n  sorters {\n    option {\n      ...SorterFields\n      __typename\n    }\n    __typename\n  }\n  oneOfThreeDeal {\n    ...OneOfThreeDeal\n    __typename\n  }\n  zeroResultsSection {\n    ...ZeroResultsSection\n    __typename\n  }\n  rocketmilesSearchUuid\n  previousSearches {\n    ...PreviousSearches\n    __typename\n  }\n  frontierThemes {\n    ...FrontierThemes\n    __typename\n  }\n  __typename\n}\n\nfragment BasicPropertyData on SearchResultProperty {\n  acceptsWalletCredit\n  basicPropertyData {\n    accommodationTypeId\n    id\n    isTestProperty\n    location {\n      address\n      city\n      countryCode\n      __typename\n    }\n    pageName\n    ufi\n    photos {\n      main {\n        highResUrl {\n          relativeUrl\n          __typename\n        }\n        lowResUrl {\n          relativeUrl\n          __typename\n        }\n        highResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        lowResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    reviewScore: reviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      showScore\n      secondaryScore\n      secondaryTextTag {\n        translation\n        __typename\n      }\n      showSecondaryScore\n      __typename\n    }\n    externalReviewScore: externalReviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      showScore\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    alternativeExternalReviewsScore: alternativeExternalReviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      showScore\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    starRating {\n      value\n      symbol\n      caption {\n        translation\n        __typename\n      }\n      tocLink {\n        translation\n        __typename\n      }\n      showAdditionalInfoIcon\n      __typename\n    }\n    isClosed\n    paymentConfig {\n      installments {\n        minPriceFormatted\n        maxAcceptCount\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  badges {\n    caption {\n      translation\n      __typename\n    }\n    closedFacilities {\n      startDate\n      endDate\n      __typename\n    }\n    __typename\n  }\n  customBadges {\n    showIsWorkFriendly\n    showParkAndFly\n    showSkiToDoor\n    showBhTravelCreditBadge\n    showOnlineCheckinBadge\n    __typename\n  }\n  description {\n    text\n    __typename\n  }\n  displayName {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  geniusInfo {\n    benefitsCommunication {\n      header {\n        title\n        __typename\n      }\n      items {\n        title\n        __typename\n      }\n      __typename\n    }\n    geniusBenefits\n    geniusBenefitsData {\n      hotelCardHasFreeBreakfast\n      hotelCardHasFreeRoomUpgrade\n      sortedBenefits\n      __typename\n    }\n    showGeniusRateBadge\n    __typename\n  }\n  location {\n    displayLocation\n    mainDistance\n    publicTransportDistanceDescription\n    skiLiftDistance\n    beachDistance\n    nearbyBeachNames\n    beachWalkingTime\n    geoDistanceMeters\n    __typename\n  }\n  mealPlanIncluded {\n    mealPlanType\n    text\n    __typename\n  }\n  persuasion {\n    autoextended\n    geniusRateAvailable\n    highlighted\n    preferred\n    preferredPlus\n    showNativeAdLabel\n    nativeAdId\n    nativeAdsCpc\n    nativeAdsTracking\n    bookedXTimesMessage\n    sponsoredAdsData {\n      isDsaCompliant\n      legalEntityName\n      sponsoredAdsDesign\n      __typename\n    }\n    __typename\n  }\n  policies {\n    showFreeCancellation\n    showNoPrepayment\n    enableJapaneseUsersSpecialCase\n    __typename\n  }\n  ribbon {\n    ribbonType\n    text\n    __typename\n  }\n  recommendedDate {\n    checkin\n    checkout\n    lengthOfStay\n    __typename\n  }\n  showGeniusLoginMessage\n  showPrivateHostMessage\n  soldOutInfo {\n    isSoldOut\n    messages {\n      text\n      __typename\n    }\n    alternativeDatesMessages {\n      text\n      __typename\n    }\n    __typename\n  }\n  nbWishlists\n  visibilityBoosterEnabled\n  showAdLabel\n  isNewlyOpened\n  propertySustainability {\n    isSustainable\n    tier {\n      type\n      __typename\n    }\n    facilities {\n      id\n      __typename\n    }\n    certifications {\n      name\n      __typename\n    }\n    chainProgrammes {\n      chainName\n      programmeName\n      __typename\n    }\n    levelId\n    __typename\n  }\n  seoThemes {\n    caption\n    __typename\n  }\n  relocationMode {\n    distanceToCityCenterKm\n    distanceToCityCenterMiles\n    distanceToOriginalHotelKm\n    distanceToOriginalHotelMiles\n    phoneNumber\n    __typename\n  }\n  bundleRatesAvailable\n  recommendedDatesLabel\n  __typename\n}\n\nfragment Banner on Banner {\n  name\n  type\n  isDismissible\n  showAfterDismissedDuration\n  position\n  requestAlternativeDates\n  title {\n    text\n    __typename\n  }\n  imageUrl\n  paragraphs {\n    text\n    __typename\n  }\n  metadata {\n    key\n    value\n    __typename\n  }\n  pendingReviewInfo {\n    propertyPhoto {\n      lowResUrl {\n        relativeUrl\n        __typename\n      }\n      lowResJpegUrl {\n        relativeUrl\n        __typename\n      }\n      __typename\n    }\n    propertyName\n    urlAccessCode\n    __typename\n  }\n  nbDeals\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  secondaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  iconName\n  flexibleFilterOptions {\n    optionId\n    filterName\n    __typename\n  }\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  dateFlexQueryOptions {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    isApplied\n    __typename\n  }\n  __typename\n}\n\nfragment Carousel on Carousel {\n  aggregatedCountsByFilterId\n  carouselId\n  position\n  contentType\n  hotelId\n  name\n  soldoutProperties\n  priority\n  themeId\n  title {\n    text\n    __typename\n  }\n  slides {\n    captionText {\n      text\n      __typename\n    }\n    name\n    photoUrl\n    subtitle {\n      text\n      __typename\n    }\n    type\n    title {\n      text\n      __typename\n    }\n    action {\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DestinationLocation on DestinationLocation {\n  name {\n    text\n    __typename\n  }\n  inName {\n    text\n    __typename\n  }\n  countryCode\n  __typename\n}\n\nfragment FilterData on Filter {\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  trackOnClick {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  name\n  field\n  category\n  filterStyle\n  title {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  subtitle\n  options {\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnViewPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    ...FilterOption\n    __typename\n  }\n  filterLayout {\n    isCollapsable\n    collapsedCount\n    __typename\n  }\n  stepperOptions {\n    min\n    max\n    default\n    selected\n    title {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    field\n    labels {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    __typename\n  }\n  sliderOptions {\n    min\n    max\n    minSelected\n    maxSelected\n    minPriceStep\n    minSelectedFormatted\n    currency\n    histogram\n    selectedRange {\n      translation\n      __typename\n    }\n    title\n    __typename\n  }\n  sliderOptionsPerStay {\n    min\n    max\n    minSelected\n    maxSelected\n    minPriceStep\n    minSelectedFormatted\n    currency\n    histogram\n    selectedRange {\n      translation\n      __typename\n    }\n    title\n    __typename\n  }\n  __typename\n}\n\nfragment FilterOption on Option {\n  optionId: id\n  count\n  selected\n  urlId\n  additionalLabel {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  value {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  starRating {\n    value\n    symbol\n    caption {\n      translation\n      __typename\n    }\n    showAdditionalInfoIcon\n    __typename\n  }\n  __typename\n}\n\nfragment LandingPageBreadcrumb on LandingPageBreadcrumb {\n  destType\n  name\n  urlParts\n  __typename\n}\n\nfragment MatchingUnitConfigurations on SearchResultProperty {\n  matchingUnitConfigurations {\n    commonConfiguration {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    unitConfigurations {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      apartmentRooms {\n        config {\n          roomId: id\n          roomType\n          bedTypeId\n          bedCount: count\n          __typename\n        }\n        roomName: tag {\n          tag\n          translation\n          __typename\n        }\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyBlocks on SearchResultProperty {\n  blocks {\n    blockId {\n      roomId\n      occupancy\n      policyGroupId\n      packageId\n      mealPlanId\n      __typename\n    }\n    finalPrice {\n      amount\n      currency\n      __typename\n    }\n    originalPrice {\n      amount\n      currency\n      __typename\n    }\n    onlyXLeftMessage {\n      tag\n      variables {\n        key\n        value\n        __typename\n      }\n      translation\n      __typename\n    }\n    freeCancellationUntil\n    hasCrib\n    blockMatchTags {\n      childStaysForFree\n      __typename\n    }\n    thirdPartyInventoryContext {\n      isTpiBlock\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PriceDisplayInfoIrene on PriceDisplayInfoIrene {\n  badges {\n    name {\n      translation\n      __typename\n    }\n    tooltip {\n      translation\n      __typename\n    }\n    style\n    identifier\n    __typename\n  }\n  chargesInfo {\n    translation\n    __typename\n  }\n  displayPrice {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  priceBeforeDiscount {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  rewards {\n    rewardsList {\n      termsAndConditions\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      breakdown {\n        productType\n        amountPerStay {\n          amount\n          amountRounded\n          amountUnformatted\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    rewardsAggregated {\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      copy {\n        translation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  useRoundedAmount\n  discounts {\n    amount {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    name {\n      translation\n      __typename\n    }\n    description {\n      translation\n      __typename\n    }\n    itemType\n    productId\n    __typename\n  }\n  excludedCharges {\n    excludeChargesAggregated {\n      copy {\n        translation\n        __typename\n      }\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    excludeChargesList {\n      chargeMode\n      chargeInclusion\n      chargeType\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  taxExceptions {\n    shortDescription {\n      translation\n      __typename\n    }\n    longDescription {\n      translation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BookerExperienceData on SearchResultProperty {\n  bookerExperienceContentUIComponentProps {\n    ... on BookerExperienceContentLoyaltyBadgeListProps {\n      badges {\n        variant\n        key\n        title\n        popover\n        logoSrc\n        logoAlt\n        __typename\n      }\n      __typename\n    }\n    ... on BookerExperienceContentFinancialBadgeProps {\n      paymentMethod\n      backgroundColor\n      hideAccepted\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SearchMetadata on SearchMeta {\n  availabilityInfo {\n    hasLowAvailability\n    unavailabilityPercent\n    totalAvailableNotAutoextended\n    __typename\n  }\n  boundingBoxes {\n    swLat\n    swLon\n    neLat\n    neLon\n    type\n    __typename\n  }\n  childrenAges\n  dates {\n    checkin\n    checkout\n    lengthOfStayInDays\n    __typename\n  }\n  destId\n  destType\n  maxLengthOfStayInDays\n  nbRooms\n  nbAdults\n  nbChildren\n  userHasSelectedFilters\n  customerValueStatus\n  affiliatePartnerChannelId\n  affiliateVerticalType\n  affiliateName\n  __typename\n}\n\nfragment SearchResultsBreadcrumb on SearchResultsBreadcrumb {\n  destId\n  destType\n  name\n  __typename\n}\n\nfragment SorterFields on SorterOption {\n  type: name\n  captionTranslationTag {\n    translation\n    __typename\n  }\n  tooltipTranslationTag {\n    translation\n    __typename\n  }\n  isSelected: selected\n  __typename\n}\n\nfragment OneOfThreeDeal on OneOfThreeDeal {\n  id\n  uuid\n  winnerHotelId\n  winnerBlockId\n  priceDisplayInfo {\n    displayPrice {\n      amountPerStay {\n        amountRounded\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  locationInfo {\n    name\n    inName\n    destType\n    __typename\n  }\n  destinationType\n  commonFacilities {\n    id\n    name\n    __typename\n  }\n  tpiParams {\n    wholesalerCode\n    rateKey\n    rateBlockId\n    bookingRoomId\n    supplierId\n    __typename\n  }\n  properties {\n    priceDisplayInfo {\n      priceBeforeDiscount {\n        amountPerStay {\n          amountRounded\n          __typename\n        }\n        __typename\n      }\n      displayPrice {\n        amountPerStay {\n          amountRounded\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    basicPropertyData {\n      id\n      name\n      pageName\n      photos {\n        main {\n          highResUrl {\n            absoluteUrl\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      location {\n        address\n        countryCode\n        __typename\n      }\n      reviews {\n        reviewsCount\n        totalScore\n        __typename\n      }\n      __typename\n    }\n    blocks {\n      thirdPartyInventoryContext {\n        rateBlockId\n        rateKey\n        wholesalerCode\n        tpiRoom {\n          bookingRoomId\n          __typename\n        }\n        supplierId\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TripTypesData on TripTypes {\n  beach {\n    isBeachUfi\n    isEnabledBeachUfi\n    isCoastalBeachRegion\n    isBeachDestinationWithoutBeach\n    __typename\n  }\n  ski {\n    isSkiExperience\n    isSkiScaleUfi\n    __typename\n  }\n  carouselBeach {\n    name\n    beachId\n    photoUrl\n    reviewScore\n    reviewScoreFormatted\n    translatedBeachActivities\n    translatedSandType\n    __typename\n  }\n  skiLandmarkData {\n    resortId\n    slopeTotalLengthFormatted\n    totalLiftsCount\n    __typename\n  }\n  __typename\n}\n\nfragment ZeroResultsSection on ZeroResultsSection {\n  title {\n    text\n    __typename\n  }\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      __typename\n    }\n    __typename\n  }\n  paragraphs {\n    text\n    __typename\n  }\n  type\n  __typename\n}\n\nfragment PreviousSearches on PreviousSearch {\n  childrenAges\n  __typename\n}\n\nfragment FrontierThemes on FrontierTheme {\n  id\n  name\n  selected\n  __typename\n}\n\nfragment geniusVipEnrolledProgram on GeniusVipEnrolledProgram {\n  metadata {\n    programType\n    __typename\n  }\n  geniusVipUIs {\n    searchResultModal {\n      title {\n        text\n        __typename\n      }\n      subtitle {\n        text\n        __typename\n      }\n      modalCategory\n      asset {\n        __typename\n        ... on Image {\n          url\n          __typename\n        }\n      }\n      cta {\n        text\n        actionString\n        actionDismiss\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
    }

    response = requests.post('https://www.booking.com/dml/graphql', params=params, headers=headers, json=json_data)
    return response
def get_imageing2(keyword):
    headers = {
        'authority': 'www.ca.kayak.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-CN;q=0.7,en-US;q=0.6,en-CA;q=0.5',
        # 'content-length': '0',
        # 'cookie': 'Apache=TES6rw-AAABi3iO_jY-ca-HiYlgw; kanid=; kanlabel=; kayak=ZRgVLarPBu7BCsgZuvRY; csid=3a4d96a7-1087-4373-b4d2-77b8084517d5; kmkid=AzWZONFPPpczOfKT6SIXRdY; _gcl_au=1.1.977708422.1698534720; _fbp=fb.1.1698534720000.0.83877501037026; __gads=ID=73819b9a526939f8:T=1698530499:RT=1698540238:S=ALNI_MYPUp5g0Wv_u62onGeU-pOluWGERA; __gpi=UID=00000d9d43481b06:T=1698530499:RT=1698540238:S=ALNI_MYizyZ1B0zDAG-EfLJooBLy36TvpQ; cluster=4; p1.med.token=XlQJE6qKOgyb9yEee_SM2D; p1.med.sid=R-4vkuYPCqEg1MqMta_SYW5-R8vJdqYxl3Bl2DHw0jJdajgabF5VRfTa9Z6zp1e1K; _uetsid=6614126075e711ee80b143ab187e5dcf; _uetvid=c31415203bb311ee9d86293a66b74360; mst_ADIrkw=BHfzRwUtpK4O-a8jqKclhvw2aObLBMJHq_utDuzZkmHR_g6rdcAu-lFFqF29TWoIXnvTrZ8B1K5ER34yIh_LTg; kayak.mc=ASah5IW0BAccsSXgKMDuedcgVaRAZPmDT0Ri-jyIyrzUOQgtn67TWeNQIgbEGhigavY9IPuX6OrhdmGv5cj6B4dx1CElwcvxkRzXNpCUM-7qFBfTCavRZhSbAC8XMzXoFCiiqHD8V2oBPz8wlArd3nkxva9LhCWLf1Tor7Hri_NvKoNmb1WmtM-0cOX6a8nKs5qu60ygxKGQo5sqCDWHcl2UVfEuigGPlJzNA4-vjOOSFNwKFGe2juCsXuSkbr2KS_6U8vhBtwP-Q7knCr_yfca-vrSi4_zGidiwFLkwEHzNgvhp1-e8PuhVEeoh-UVHXGVtWcgPZHYY7O_xTyWgp6FwMkFp4bhJf3Mc2MSPvPrqAzWfCUkkidHTzxtO3LbelVMr8FEpklpMm9bod4G-0Qmwkz_zYoa03G9RLwgpzii9; mst_iBfK2g=ts-pUdsQFf95kQewhYhZFW7wqiZWA67vJpmOPbYBujaxa7uqVFV7ERLV41Rgq31DEShlfrGxRUQrha8Q6TbeRA',
        'origin': 'https://www.ca.kayak.com',
        'referer': 'https://www.ca.kayak.com/stays',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'f': 'j',
        's': '50',
        'where': keyword,
        'lc_cc': 'CA',
        'lc': 'en',
        'sv': '5',
        'cv': 'undefined',
        'c': 'undefined',
        'searchId': 'undefined',
        'v': 'undefined',
    }

    response = requests.post('https://www.ca.kayak.com/mvm/smartyv2/search', params=params, headers=headers)
    return response.json()
if __name__=='__main__':
    aa=Get_booking_hotel('NewYork','2023-10-15','2023-10-16').json()
    list_data=aa['data']['searchQueries']['search']['results']
    Hotel_name_list=[]#['displayName']['text']
    Location_list=[]#['location']['displayLocation']
    # description_list=[]
    Image_list=[]#['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl']
    score_list=[]#['basicPropertyData']['reviewScore']['score']
    Price_list=[]#['blocks']['finalPrice']['amount']
    address_list=[]#['basicPropertyData']['location']
    for each_data in list_data:
        Hotel_name=each_data['displayName']['text']
        Location=each_data['location']['displayLocation']
        Images=each_data['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl']#'https://cf.bstatic.com/'+
        score=each_data['basicPropertyData']['reviewScore']['score']
        Price=each_data['blocks'][0]['finalPrice']['amount']
        address=each_data['basicPropertyData']['location']
        Hotel_name_list.append(Hotel_name)
        Location_list.append(Location)
        Image_list.append(Image_list)
        score_list.append(score)
        Price_list.append(Price)
        address_list.append(address)
    print(Location_list)